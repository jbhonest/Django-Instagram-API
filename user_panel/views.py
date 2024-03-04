from django_filters.rest_framework import DjangoFilterBackend
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework import viewsets, filters, generics
from rest_framework import permissions
from rest_framework.mixins import DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from .models import Follow, CustomUser
from .serializers import FollowSerializer, UserProfileSerializer, UserListSerializer, RegisterSerializer, PublicFollowSerializer


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = ('follower', 'following')

    def get_queryset(self):
        return Follow.objects.filter(follower=self.request.user.id)

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            return Response({'error': 'You have already followed this user.'}, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(follower=self.request.user)


class UserProfileViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin,
                         DestroyModelMixin,
                         viewsets.GenericViewSet):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = ('username',)

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)


class PublicUsersViewSet(ListModelMixin, RetrieveModelMixin,
                         viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserListSerializer
    queryset = CustomUser.objects.filter(is_public=True).order_by('-pk')
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = ('username', 'email', 'first_name', 'last_name')


class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=serializer.instance)
        return Response({
            "user": UserProfileSerializer(user, context=self.get_serializer_context()).data
        })


class PublicFollowViewSet(ListModelMixin, RetrieveModelMixin,
                          viewsets.GenericViewSet):
    queryset = Follow.objects.filter(follower__is_public=True).order_by('-pk')
    serializer_class = PublicFollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = ('follower', 'following')
