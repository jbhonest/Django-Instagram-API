from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Follow, CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {
         'fields': ('first_name', 'last_name', 'email', 'is_public')}),
        ('Permissions', {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('id', 'username', 'email', 'first_name',
                    'last_name', 'is_staff', 'is_active', 'is_public')
    search_fields = ('username', 'email', 'first_name',
                     'last_name', 'is_public')
    ordering = ('id',)
    list_filter = ['is_active', 'is_public', 'is_staff']


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ['follower', 'following', 'created_at']
    search_fields = ['follower__username', 'following__username']
    list_filter = ['created_at', 'follower', 'following']
