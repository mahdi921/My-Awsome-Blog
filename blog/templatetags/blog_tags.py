from django import template
from blog.models import Post
from django.db.models import Count
from django.utils import timezone
from django.contrib.auth.models import User

register = template.Library()

@register.inclusion_tag('blog/blog-author-widget.html')
def blog_author():
    popular_author = Post.objects.filter(author__isnull=False).values('author').annotate(post_count=Count('id')).order_by('-post_count')[0]
    author = User.objects.get(id=popular_author['author'])
    return {'author': author}

@register.inclusion_tag('blog/blog-popular-posts.html')
def popular_widget(qty=5):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1).order_by('-counted_views')[:qty]
    return {'posts' : posts}