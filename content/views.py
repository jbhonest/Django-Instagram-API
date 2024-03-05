from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, permissions
from .models import Post, Image, Mention, Hashtag
from .serializers import PostSerializer, ImageSerializer, MentionSerializer, HashtagSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.order_by('-pk')
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = ('user',)
    search_fields = ('caption',)

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user.id).order_by('-pk')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = ('post',)

    def get_queryset(self):
        return Image.objects.filter(post__user=self.request.user.id).order_by('-pk')

    def perform_create(self, serializer):
        # Ensure the user can only add images to their own posts
        post_id = self.request.data.get('post', None)
        post = get_object_or_404(Post, id=post_id, user=self.request.user)
        serializer.save(post=post)


class MentionViewSet(viewsets.ModelViewSet):
    serializer_class = MentionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = ('post', 'user')

    def get_queryset(self):
        return Mention.objects.filter(post__user=self.request.user.id).order_by('-pk')

    def perform_create(self, serializer):
        # Ensure the user can only add mentions to their own posts
        post_id = self.request.data.get('post', None)
        post = get_object_or_404(Post, id=post_id, user=self.request.user)
        serializer.save(post=post)


class HashtagViewSet(viewsets.ModelViewSet):
    serializer_class = HashtagSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = ('post', 'title')

    def get_queryset(self):
        return Hashtag.objects.filter(post__user=self.request.user.id).order_by('-pk')

    def perform_create(self, serializer):
        # Ensure the user can only add hashtag to their own posts
        post_id = self.request.data.get('post', None)
        post = get_object_or_404(Post, id=post_id, user=self.request.user)
        serializer.save(post=post)
