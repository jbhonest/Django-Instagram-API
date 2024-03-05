from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, permissions
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from .models import Post, Story, PostImage, StoryImage, Mention, Hashtag
from .serializers import PostSerializer, PostImageSerializer, MentionSerializer, HashtagSerializer, StoryImageSerializer, StorySerializer
from django.contrib.auth import get_user_model

User = get_user_model()


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


class StoryViewSet(viewsets.ModelViewSet):
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Story.objects.order_by('-pk')
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = ('user',)

    def get_queryset(self):
        return Story.objects.filter(user=self.request.user.id).order_by('-pk')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class PostImageViewSet(viewsets.ModelViewSet):
    serializer_class = PostImageSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = ('post',)

    def get_queryset(self):
        return PostImage.objects.filter(post__user=self.request.user.id).order_by('-pk')

    def perform_create(self, serializer):
        # Ensure the user can only add images to their own posts
        post_id = self.request.data.get('post', None)
        post = get_object_or_404(Post, id=post_id, user=self.request.user)
        serializer.save(post=post)


class StoryImageViewSet(viewsets.ModelViewSet):
    serializer_class = StoryImageSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = ('story',)

    def get_queryset(self):
        return StoryImage.objects.filter(story__user=self.request.user.id).order_by('-pk')

    def perform_create(self, serializer):
        # Ensure the user can only add images to their own stories
        story_id = self.request.data.get('story', None)
        story = get_object_or_404(
            Story, id=story_id, user=self.request.user)
        serializer.save(story=story)


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


class FollowingPostViewSet(ListModelMixin, RetrieveModelMixin,
                           viewsets.GenericViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.order_by('-pk')
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = ('user',)
    search_fields = ('caption',)

    def get_queryset(self):
        user_profile = User.objects.get(id=self.request.user.id)
        following = user_profile.following.all()
        following_ids = (user.id for user in following)
        return Post.objects.filter(user__in=following_ids).order_by('-pk')
