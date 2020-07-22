from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm

def index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts':posts})


def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    commentForm = CommentForm()
    return render(request, 'post/detail.html', {'post':post, 'commentForm':commentForm})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('detail', id=post.pk)
    else:
        form = PostForm()
    return render(request, 'post/edit_form.html', {'form':form})

def post_edit(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid(): 
            post = form.save(commit = False)
            post.save()
            return redirect('detail', id=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post/edit_form.html', {'form':form})    

def post_delete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect('index')


def comment_new(request, id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = get_object_or_404(Post, pk=id)
            comment.save()
            return redirect('detail', id=id)
    else:
        return redirect('index')

def comment_delete(request, id):
    comment = get_object_or_404(Comment, pk=id)
    comment.delete()
    return redirect('index')