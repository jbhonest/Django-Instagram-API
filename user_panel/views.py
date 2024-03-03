from django_filters.rest_framework import DjangoFilterBackend
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework import viewsets, filters
from rest_framework import permissions
from rest_framework.mixins import DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from .models import Follow, CustomUser
from .serializers import FollowSerializer, UserProfileSerializer, UserListSerializer


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.order_by('-pk')
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = ('follower', 'following')

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


class UserViewSet(ListModelMixin, RetrieveModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = UserListSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = ('username',)

    def get_queryset(self):
        return CustomUser.objects.order_by('-pk')


class UserRegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = CustomUser.objects.none()
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
