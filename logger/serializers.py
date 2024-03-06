from rest_framework import serializers
from .models import PostView
from user_panel.serializers import SimpleUserSerializer


class PostViewSerializer(serializers.ModelSerializer):
    viewer = SimpleUserSerializer()

    class Meta:
        model = PostView
        fields = ('id', 'post', 'viewer')
