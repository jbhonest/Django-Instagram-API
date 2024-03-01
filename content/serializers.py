from rest_framework import serializers
from .models import Post, Image, Mention, Hashtag
from user_activity.models import Comment, Like


class SimpleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image', 'created_at']


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


class SimpleLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    images = SimpleImageSerializer(many=True, read_only=True)
    hashtags = SimpleHashtagSerializer(many=True, read_only=True)
    comments = SimpleCommentSerializer(many=True, read_only=True)
    likes = SimpleLikeSerializer(many=True, read_only=True)
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


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'post', 'image', 'created_at')


class MentionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mention
        fields = ('id', 'post', 'user', 'created_at')


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ('id', 'post', 'title', 'created_at')
