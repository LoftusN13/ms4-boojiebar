from django import forms
from .widgets import CustomClearableFileInput
from .models import BlogPost, Comment


class BlogForm(forms.ModelForm):
    # form to create new blog
    class Meta:
        model = BlogPost
        fields = ('__all__')

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)


class CommentForm(forms.ModelForm):
    # form to create new blog comment
    class Meta:
        model = Comment
        fields = (
            'user',
            'body'
        )
