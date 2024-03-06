from django.contrib import admin
from .models import PostView, ProfileView


@admin.register(PostView)
class PostViewAdmin(admin.ModelAdmin):
    list_display = ('id',  'post', 'viewer', 'created_at')
    list_filter = ('post', 'viewer', 'created_at')


@admin.register(ProfileView)
class PostViewAdmin(admin.ModelAdmin):
    list_display = ('id',  'profile', 'viewer', 'created_at')
    list_filter = ('profile', 'viewer', 'created_at')
