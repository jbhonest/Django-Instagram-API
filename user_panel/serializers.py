from rest_framework import serializers
from .models import Follow, CustomUser


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username']


class FollowSerializer(serializers.ModelSerializer):
    follower = SimpleUserSerializer(read_only=True)
    following_info = SimpleUserSerializer(source='following', read_only=True)

    class Meta:
        model = Follow
        fields = ['id', 'follower', 'following',
                  'following_info', 'created_at']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password',
                  'email', 'first_name', 'last_name', 'is_public')
        extra_kwargs = {'password': {'write_only': True}}


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email',
                  'first_name', 'last_name', 'is_public')
