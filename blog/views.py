from django.shortcuts import render
from .models import BlogPost

# Create your views here.


def all_blog_posts(request):
    """
    view to return all blog posts.

    """
    blogs = BlogPost.objects.all()
    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/blog_posts.html', context)
