from django_filters.rest_framework import DjangoFilterBackend
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, filters
from rest_framework import permissions
from .models import Follow, CustomUser
from .serializers import FollowSerializer, UserProfileSerializer


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


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = ('username',)

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)


class UserRegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = CustomUser.objects.none()
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
