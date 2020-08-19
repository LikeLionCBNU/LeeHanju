from django.shortcuts import render
from .models import BookMark
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class BookmarkListView(ListView):
    model = BookMark

#Create Bookmark 메서드 추가
class BookmarkCreateView(CreateView):
    model = BookMark
    fields = ['site_name','url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'    

#View Detail Bookmark 메서드 추가
class BookmarkDetailView(DetailView):
    model = BookMark

#Update View Bookmark 메서드 추가
class BookmarkUpdateView(UpdateView):
    model = BookMark
    fields = ['site_name','url']
    template_name_suffix = '_update'
    success_url =  reverse_lazy('list')

#Delete View Bookmark 메서드 추가
class BookmarkDeleteView(DeleteView):
    model = BookMark
    success_url = reverse_lazy('list')