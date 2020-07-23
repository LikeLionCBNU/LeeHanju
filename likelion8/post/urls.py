
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('post_new/', views.post_new, name='post_new'),
    path('edit/<int:id>', views.post_edit, name='post_edit'),
    path('delete/<int:id>', views.post_delete, name='post_delete'),
    path('comment_new/<int:id>', views.comment_new, name='comment_new'),
    path('comment_delete/<int:id>', views.comment_delete, name="comment_delete"),
    path('comment_edit/<int:id>', views.comment_edit, name="comment_edit"),
]
