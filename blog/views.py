from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from blog.forms import CommentForm

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
    comments = Comment.objects.filter(post=post, approved=True).order_by('-created_date')
    if request.method == 'POST':
        from django.contrib import messages
        form = CommentForm(request.POST)
        if form.is_valid():
            new_instance = form.save(commit=False)
            if new_instance.subject == '':
                new_instance.subject = '-empty-'
            new_instance.post = post
            new_instance.save()
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your comment has been submitted and is awaiting approval')
        elif form.errors:
            messages.add_message(request, messages.ERROR, 'Your comment didnt go through, check your input')
    form = CommentForm()
    context = {
        'post' : post,
        'next' : next_post,
        'previous' : previous_post,
        "comments" : comments,
        'form' : form,
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