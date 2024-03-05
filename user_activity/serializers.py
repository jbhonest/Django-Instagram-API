from rest_framework import serializers
from .models import Comment, PostLike, StoryLike


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'post', 'text', 'user', 'created_at')

    def get_fields(self):
        fields = super().get_fields()
        if 'user' in fields:
            # Make user field read_only in the browsable API
            fields['user'].read_only = True
        return fields


class PostLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostLike
        fields = ('id', 'post', 'user', 'created_at')

    def get_fields(self):
        fields = super().get_fields()
        if 'user' in fields:
            # Make user field read_only in the browsable API
            fields['user'].read_only = True
        return fields


class StoryLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = StoryLike
        fields = ('id', 'story_image', 'user', 'created_at')

    def get_fields(self):
        fields = super().get_fields()
        if 'user' in fields:
            # Make user field read_only in the browsable API
            fields['user'].read_only = True
        return fields
