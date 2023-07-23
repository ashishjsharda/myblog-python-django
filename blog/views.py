from django.shortcuts import render
from .models import Post

def list_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/list_posts.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        post = Post()
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        Post.objects.create(title=post.title, content=post.content)
        return render(request, 'blog/post_created.html')
