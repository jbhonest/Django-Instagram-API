from rest_framework import serializers
from .models import PostView, ProfileView
from user_panel.serializers import SimpleUserSerializer


class PostViewSerializer(serializers.ModelSerializer):
    viewer = SimpleUserSerializer()

    class Meta:
        model = PostView
        fields = ('id', 'post', 'viewer')


class ProfileViewSerializer(serializers.ModelSerializer):
    viewer = SimpleUserSerializer()

    class Meta:
        model = ProfileView
        fields = ('id', 'profile', 'viewer')
