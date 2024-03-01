from django.contrib import admin
from django.db.models import Count
from .models import Post, Image, Mention
from user_activity.models import Comment


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'caption', 'user', 'comment_count', 'created_at')
    list_filter = ('user', 'created_at')
    search_fields = ('caption',)
    inlines = [ImageInline, CommentInline]

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(comment_count=Count('comments'))

    @admin.display(ordering='comment_count')
    def comment_count(self, post):
        return post.comments.count()


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'image', 'created_at')
    list_filter = ('post', 'created_at')


@admin.register(Mention)
class MentionAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'created_at')
    list_filter = ('post', 'user', 'created_at')
