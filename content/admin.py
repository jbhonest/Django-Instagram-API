from django.contrib import admin
from django.db.models import Count
from .models import Post, Story, PostImage, StoryImage, Mention, Hashtag
from user_activity.models import Comment


class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1


class StoryImageInline(admin.TabularInline):
    model = StoryImage
    extra = 1


class HashtagInline(admin.TabularInline):
    model = Hashtag
    extra = 1


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class MentionInline(admin.TabularInline):
    model = Mention
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'caption', 'user', 'comment_count', 'created_at')
    list_filter = ('user', 'created_at')
    search_fields = ('caption',)
    inlines = [PostImageInline, HashtagInline, MentionInline, CommentInline]

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(comment_count=Count('comments'))

    @admin.display(ordering='comment_count')
    def comment_count(self, post):
        return post.comments.count()


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('id',  'user',  'created_at')
    list_filter = ('user', 'created_at')
    inlines = [StoryImageInline]


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'image', 'created_at')
    list_filter = ('post', 'created_at')


@admin.register(StoryImage)
class StoryImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'story', 'image', 'created_at')
    list_filter = ('story', 'created_at')


@admin.register(Mention)
class MentionAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'created_at')
    list_filter = ('post', 'user', 'created_at')


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'title', 'created_at')
    list_filter = ('post', 'title', 'created_at')
