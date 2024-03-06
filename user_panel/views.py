from django_filters.rest_framework import DjangoFilterBackend
from django.db import IntegrityError
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework import viewsets, filters, generics
from rest_framework import permissions
from rest_framework.mixins import DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from logger.models import ProfileView
from .models import Follow, CustomUser, Profile
from .serializers import FollowSerializer, UserAccountSerializer, PublicProfilesSerializer, RegisterSerializer, PublicFollowSerializer, ProfileSerializer


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = ('follower', 'following')

    def get_queryset(self):
        return Follow.objects.filter(follower=self.request.user.id).order_by('-pk')

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            return Response({'error': 'You have already followed this user.'}, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(follower=self.request.user)


class UserAccountViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin,
                         DestroyModelMixin,
                         viewsets.GenericViewSet):
    serializer_class = UserAccountSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = ('username',)

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)


class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Create a profile for the registered user
        Profile.objects.create(user=user)

        token, _ = Token.objects.get_or_create(user=serializer.instance)
        return Response({
            "user": UserAccountSerializer(user, context=self.get_serializer_context()).data
        })


class PublicProfilesViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PublicProfilesSerializer
    queryset = Profile.objects.filter(user__is_public=True).order_by('-pk')
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = ('user', )

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        profile = self.get_object()
        # Trigger the profile view signal
        post_save.send(sender=Profile, instance=profile,
                       created=False, request=request)
        return response


class FollowingProfilesViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PublicProfilesSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = ('user',)

    def get_queryset(self):
        # Get the profiles of users whom the authenticated user is following
        users = self.request.user.following.all()
        following_users = (f.following for f in users)
        following_profiles = Profile.objects.filter(user__in=following_users)
        return following_profiles


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user.id).order_by('-pk')

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        profile = self.get_object()
        # Trigger the profile view signal
        post_save.send(sender=Profile, instance=profile,
                       created=False, request=request)
        return response


@receiver(post_save, sender=Profile)
def log_profile_view(sender, instance, created, **kwargs):
    if not created:
        request = kwargs.get('request')
        if hasattr(request, 'user'):
            ProfileView.objects.create(profile=instance, viewer=request.user)
