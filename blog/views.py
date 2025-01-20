from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.

def blog_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(),
                                status=1)
    posts = Paginator(posts, 6)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    context = {
        'posts' : posts
    }
    return render(request, 'blog/blog-home.html', context)

def blog_single_view(request, pid):
    post = get_object_or_404(Post, id=pid, status=1,
                             published_date__lte=timezone.now())
    post.counted_views += 1
    post.save()
    other_posts = Post.objects.filter(published_date__lte=timezone.now(), status=1).exclude(id=pid)
    next_post = other_posts.filter(id__gt=pid).order_by('id').first()
    previous_post = other_posts.filter(id__lt=pid).order_by('-id').first()
    context = {
        'post' : post,
        'next' : next_post,
        'previous' : previous_post
    }
    return render(request, 'blog/single-post.html', context)