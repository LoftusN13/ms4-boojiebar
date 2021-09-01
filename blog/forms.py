from django import forms
from .widgets import CustomClearableFileInput
from .models import BlogPost


class BlogForm(forms.ModelForm):
    # form to create new blog
    class Meta:
        model = BlogPost
        fields = ('__all__')

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)
