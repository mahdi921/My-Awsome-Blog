from django.shortcuts import render
from django.http import HttpResponseRedirect
from website.forms import NewsletterForm, ContactForm
from django.contrib import messages
from blog.models import Post
from django.utils import timezone

# Create your views here.

def index_view(request):
    post = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-counted_views')[0]
    return render(request, 'website/index.html',{'post':post})

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            new_instance = form.save(commit=False)
            new_instance.name = 'Anonymous'
            new_instance.save()
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your message has been sent')
        elif form.errors:
            messages.add_message(request, messages.ERROR, 'Your message has not been sent, check your input')
    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})
    # return render(request, 'website/contact.html')

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')