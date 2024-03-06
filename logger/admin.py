from django.contrib import admin
from .models import PostView


@admin.register(PostView)
class PostViewAdmin(admin.ModelAdmin):
    list_display = ('id',  'post', 'viewer', 'created_at')
    list_filter = ('post', 'viewer', 'created_at')
