from django.db import models
from django.conf import settings


class Post(models.Model):
    caption = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def delete(self):
        # Delete associated Image objects and their image files
        for image in self.images.all():
            image.delete()

        # Call the superclass's delete method
        super().delete()

    def __str__(self):
        return self.caption


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='post_comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Image(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='content_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def delete(self):
        # Delete the image file from the storage
        storage, path = self.image.storage, self.image.path
        storage.delete(path)

        # Call the parent class's delete method to remove the model instance from the database
        super().delete()

    def __str__(self):
        return str(self.id)
