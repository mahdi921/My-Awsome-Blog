from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render(request, 'blog/index.html')

def about_view(request):
    return render(request, 'blog/about.html')

def contact_view(request):
    return render(request, 'blog/contact.html')