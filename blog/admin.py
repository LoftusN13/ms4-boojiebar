from django.contrib import admin
from .models import BlogPost, Comment

# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
    # Admin display for blog post
    list_display = (
        'title',
        'author',
        'created_at',
    )
    search_fields = ['title', 'body']


class CommentAdmin(admin.ModelAdmin):
    # Admin display for blog comments
    list_display = (
        'user',
        'body',
        'post',
        'created_on',
        )

    list_filter = ('created_on',)

    search_fields = ['user', 'body']


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)
