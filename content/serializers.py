from rest_framework import serializers
from .models import Post, Story, PostImage, StoryImage, Mention, Hashtag
from user_activity.models import Comment, PostLike, StoryLike


class SimplePostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['id', 'image', 'created_at']


class SimpleStoryLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryLike
        fields = ['id', 'user', 'created_at']


class SimpleStoryImageSerializer(serializers.ModelSerializer):
    likes = SimpleStoryLikeSerializer(many=True, read_only=True)

    class Meta:
        model = StoryImage
        fields = ['id', 'image', 'created_at', 'likes']


class SimpleHashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ['id', 'title', 'created_at']


class SimpleMentionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mention
        fields = ['id', 'user', 'created_at']


class SimpleCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'created_at']


class SimplePostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ['id', 'user', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    images = SimplePostImageSerializer(many=True, read_only=True)
    hashtags = SimpleHashtagSerializer(many=True, read_only=True)
    comments = SimpleCommentSerializer(many=True, read_only=True)
    likes = SimplePostLikeSerializer(many=True, read_only=True)
    mentions = SimpleMentionSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'caption', 'user', 'created_at',
                  'images', 'hashtags', 'mentions', 'comments', 'likes')

    def get_fields(self):
        fields = super().get_fields()
        if 'user' in fields:
            # Make user field read_only in the browsable API
            fields['user'].read_only = True
        return fields


class StorySerializer(serializers.ModelSerializer):
    images = SimpleStoryImageSerializer(many=True, read_only=True)

    class Meta:
        model = Story
        fields = ('id',  'user', 'created_at',
                  'images')

    def get_fields(self):
        fields = super().get_fields()
        if 'user' in fields:
            # Make user field read_only in the browsable API
            fields['user'].read_only = True
        return fields


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ('id', 'post', 'image', 'created_at')


class StoryImageSerializer(serializers.ModelSerializer):
    likes = SimpleStoryLikeSerializer(many=True, read_only=True)

    class Meta:
        model = StoryImage
        fields = ('id', 'story', 'image', 'created_at', 'likes')


class MentionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mention
        fields = ('id', 'post', 'user', 'created_at')


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ('id', 'post', 'title', 'created_at')
