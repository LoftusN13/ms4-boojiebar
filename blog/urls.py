from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blog_posts, name='blogs'),
    path('<int:blog_id>/', views.blog_details, name='blog_details'),
    path('add/', views.add_blog, name='add_blog'),
    path('edit/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),
]
