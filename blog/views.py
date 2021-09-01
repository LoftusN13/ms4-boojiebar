from django.shortcuts import (
    render, redirect, reverse,
    get_object_or_404)
from django.contrib import messages

from .models import BlogPost
from .forms import BlogForm

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


def add_blog(request):
    # view to add new blog post
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save()
            messages.success(request, 'Successfully added new blog post!')
            return redirect(reverse('blog_details', args=[blog.id]))
        else:
            messages.error(request, 'Failed to add blog post. \
                Please ensure the form is valid.')
    else:
        form = BlogForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
