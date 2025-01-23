from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q


# Create your views here.

def blog_view(request, tag_name=None, author_name=None, category_name=None):
    posts = Post.objects.filter(published_date__lte=timezone.now(),
                                status=1)
    #search query handled here
    query = request.GET.get('s')
    if query:
        posts = posts.filter(Q(content__contains=query) | Q(title__contains=query))
    #tag filtering handled here
    if tag_name:
        posts = posts.filter(tag__name=tag_name)
    #author filtering handled here
    if author_name:
        posts = posts.filter(author__username=author_name)
    #category filtering handled here
    if category_name:
        posts = posts.filter(category__name=category_name)
    #pagination handled here
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

# def search_view(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now(),
#                                 status=1)
#     query = request.GET.get('s')
#     if query:
#
#         posts = posts.filter(Q(content__contains=query)|Q(title__contains=query))
#     context = {
#         'posts' : posts
#     }
#     return render(request, 'blog/blog-home.html', context)