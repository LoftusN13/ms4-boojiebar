from django.shortcuts import (
    render, redirect, reverse,
    get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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


@login_required
def add_blog(request):
    # view to add new blog post
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store owners can access that page!')
        return redirect(reverse('home'))

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


@login_required
def edit_blog(request, blog_id):
    # view to edit specific blog post
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store owners can access that page!')
        return redirect(reverse('home'))

    blog = get_object_or_404(BlogPost, pk=blog_id)

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated blog post!')
            return redirect(reverse('blog_details', args=[blog.id]))
        else:
            messages.error(request, 'Failed to update blog post. \
                Please ensure the form is valid.')
    else:
        form = BlogForm(instance=blog)
        messages.info(request, f'You are editing {blog.title}')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, template, context)


@login_required
def delete_blog(request, blog_id):
    # delete specific blog post
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store owners can access that page!')
        return redirect(reverse('home'))

    blog = get_object_or_404(BlogPost, pk=blog_id)

    blog.delete()
    messages.success(request, 'Successfully deleted blog post!')
    return redirect(reverse('blogs'))
