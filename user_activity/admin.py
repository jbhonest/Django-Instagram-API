from django.contrib import admin
from .models import Comment, Like


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'text', 'user',
                    'created_at')
    list_filter = ('post', 'user', 'created_at')
    search_fields = ('text',)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'created_at')
    list_filter = ('post', 'user', 'created_at')
