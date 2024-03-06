from rest_framework import serializers
from .models import PostView, ProfileView


class PostViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostView
        fields = '__all__'


class ProfileViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileView
        fields = '__all__'
