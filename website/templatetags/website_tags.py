from django import template
from django.utils import timezone
from blog.models import Post, Category

register = template.Library()

@register.inclusion_tag('website/index-slider-section.html')
def index_slider(arg=6):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-created_date')[:arg]
    return {'posts': posts}

@register.inclusion_tag('website/index-trending-section.html')
def index_trending(arg=5):
    trending_posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-counted_views')[:arg]
    return {'trending_posts':trending_posts}

@register.inclusion_tag('website/index-post-category.html')
def index_category(arg):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-id')
    category = Category.objects.all()
    post_list = []
    for name in category:
        post_list.append(posts.filter(category=name).first())
    if arg == 1:
        return {'posts':post_list[:3]}
    elif arg == 2:
        return {'posts':post_list[3:6]}