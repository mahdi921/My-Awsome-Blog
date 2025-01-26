from django import template
from django.utils import timezone
from blog.models import Post

register = template.Library()

@register.inclusion_tag('website/index-slider-section.html')
def index_slider(arg=6):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-created_date')[:arg]
    return {'posts': posts}