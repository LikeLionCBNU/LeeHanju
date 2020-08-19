from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='post_index'),
    path('post/<int:post_id>/', detail, name='post_detail'),
    path('post/new', new, name='post_new'),
    path('post/<int:post_id>/edit/', edit, name='post_edit'),
    path('post/<int:post_id>/delete/', delete, name='post_delete'),
    path('post/search/', search, name='post_search'),
    path('manage/', manage, name='blog_manage'),
    path('tag/<str:tag>/', TaggedObjectLV.as_view(), name='tagged_post_list'),
]