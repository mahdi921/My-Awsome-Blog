from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render(request, 'blog/index.html')

def about_view(request):
    return render(request, 'blog/about.html')

def contact_view(request):
    return render(request, 'blog/contact.html')

def blog_single_view(request, pid):
    return render(request, 'blog/single-post.html')

def blog_view(request):
    return render(request, 'blog/blog-home.html')