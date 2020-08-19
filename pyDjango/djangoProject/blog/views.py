from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.views.generic import ListView

# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-create_date');
    return render(request, 'blog/post_index.html', {'posts':posts})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post':post})

def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            tags = request.POST.get('tags', '').split(',')
            for tag in tags:
                tag = tag.strip()
                post.tags.add(tag)
            post.save()
            return redirect('post_detail', post_id=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})

def edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('post_detail', post_id=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form':form})

def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('post_index')

def search(request):
    posts = Post.objects.all().order_by('-id')
    q = request.POST.get('q', '') 
    if q:
        posts = posts.filter(title__icontains=q)
        return render(request, 'blog/post_search.html', {'posts': posts, 'q':q})
    else:
        return render(request, 'blog/post_search.html')
    
    
class TaggedObjectLV(ListView):
    template_name = 'blog/taggit_post_list.html'
    model = Post
    
    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context
    
def manage(request):
    posts = Post.objects.all()
    populars = posts.order_by('-hits')[:5]
    tags = dict()
    for post in posts:
        for t in post.tags.all():
            t = str(t)
            if (tags.get(t) == None): tags[t] = 1
            else: tags[t] = tags.get(t) + 1
    tag_values = sorted(tags.values(), reverse=True)[:3]
    s = sum(sorted(tags.values(), reverse=True)[3:])
    tag_values.append(s)

    tags = sorted(tags.items())[:3]
    tag_keys = []
    for i in tags:
        tag_keys.append(i[0])
    tag_keys.append('기타')

    return render(request, 'blog/blog_manage.html', {'posts': posts, 'populars': populars, 'tag_keys':tag_keys, 'tag_values': tag_values})