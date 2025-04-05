from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'published_date', 'video')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'published_date')
    fields = ('title', 'slug', 'content', 'video', 'author', 'is_published', 'published_date')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'created_at', 'approved')
    list_filter = ('approved', 'created_at')
    search_fields = ('content',)
