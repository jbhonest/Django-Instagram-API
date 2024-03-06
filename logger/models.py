from django.db import models
from content.models import Post
from django.conf import settings
from user_panel.models import Profile


class PostView(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    viewer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class ProfileView(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='profiles')
    viewer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
