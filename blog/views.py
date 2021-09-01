from django.shortcuts import render, get_object_or_404
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


def blog_details(request, blog_id):
    # view to return individual blog post
    blog = get_object_or_404(BlogPost, pk=blog_id)

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog_details.html', context)
