from django import template
from django.utils import timezone
from blog.models import Post

register = template.Library()

@register.inclusion_tag('website/index-slider-section.html')
def index_slider(arg=6):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-created_date')[:arg]
    return {'posts': posts}

@register.inclusion_tag('website/index-trending-section.html')
def index_trending(arg=5):
    trending_posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-counted_views')[:arg]
    return {'trending_posts':trending_posts}