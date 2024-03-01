from rest_framework import serializers
from .models import Post, Comment, Image


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
        fields = ('id', 'caption', 'user', 'images', 'comments', 'created_at')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'post', 'text', 'user')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'post', 'image')
