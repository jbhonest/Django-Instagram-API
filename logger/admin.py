from django.contrib import admin
from .models import PostView, ProfileView


@admin.register(PostView)
class PostViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'viewer', 'post', 'created_at')
    list_filter = ('viewer', 'post', 'created_at')


@admin.register(ProfileView)
class PostViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'viewer', 'profile', 'created_at')
    list_filter = ('viewer', 'profile', 'created_at')
