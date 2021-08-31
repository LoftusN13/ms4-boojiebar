from django.db import models

from profiles.models import UserProfile

# Create your models here.


class BlogPost(models.Model):
    author = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body_text = models.TextField(default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
