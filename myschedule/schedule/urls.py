from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('schedule/<int:schedule_id>/', views.detail, name='detail'),
    path('schedule/new/', views.schedule_new, name='new'),
    path('schedule/<int:schedule_id>/edit/', views.schedule_edit, name='edit'),
    path('schedule/<int:schedule_id>/delete/', views.schedule_delete, name='delete'),
]