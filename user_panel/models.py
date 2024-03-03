from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_public = models.BooleanField(default=False)


class Follow(models.Model):
    follower = models.ForeignKey(
        CustomUser, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(
        CustomUser, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['follower', 'following']
