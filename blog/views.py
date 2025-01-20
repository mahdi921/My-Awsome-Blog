from django.shortcuts import render
from blog.models import Post
from django.utils import timezone
# Create your views here.

def blog_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(),
                                status=1)
    context = {
        'psots' : posts
    }
    return render(request, 'blog/blog-home.html', context)

def blog_single_view(request, pid):

    return render(request, 'blog/single-post.html')