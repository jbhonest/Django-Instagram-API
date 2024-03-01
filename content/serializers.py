from rest_framework import serializers
from .models import Post, Image
from user_activity.models import Comment


class SimpleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image', 'created_at']


class SimpleCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    images = SimpleImageSerializer(many=True, read_only=True)
    comments = SimpleCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'caption', 'user', 'created_at', 'images', 'comments')

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
