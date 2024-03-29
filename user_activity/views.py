from rest_framework import viewsets, filters, permissions
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from django_filters.rest_framework import DjangoFilterBackend
from .models import Comment, PostLike, StoryLike
from .serializers import CommentSerializer, PostLikeSerializer, StoryLikeSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.order_by('-pk')
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = ('post', 'user')
    search_fields = ('text',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class PostLikeViewSet(viewsets.ModelViewSet):
    serializer_class = PostLikeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = ('post', 'user')

    def get_queryset(self):
        return PostLike.objects.filter(user=self.request.user.id).order_by('-pk')

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            return Response({'error': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class StoryLikeViewSet(viewsets.ModelViewSet):
    serializer_class = StoryLikeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = ('story_image', 'user')

    def get_queryset(self):
        return StoryLike.objects.filter(user=self.request.user.id).order_by('-pk')

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            return Response({'error': 'You have already liked this story image.'}, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
