from django.db import models
from django.conf import settings
from content.models import Post


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='post_comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
