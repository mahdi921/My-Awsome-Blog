from django.shortcuts import render
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

    return render(request, 'blog/single-post.html')