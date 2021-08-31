from django.contrib import admin
from .models import BlogPost

# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
    # Admin display for blog post
    list_display = (
        'title',
        'author',
        'created_at',
    )
    search_fields = ['title', 'body']


admin.site.register(BlogPost, BlogPostAdmin)
