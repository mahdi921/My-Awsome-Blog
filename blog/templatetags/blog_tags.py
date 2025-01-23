from django import template
from blog.models import Post, Category
from django.db.models import Count
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.models import Tag

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

@register.inclusion_tag('blog/blog-tags-widget.html')
def all_blog_tags():
    tags = Tag.objects.all()
    return {'tags' : tags}

@register.inclusion_tag('blog/blog-categories-widget.html')
def category_widget():
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
    category = Category.objects.all()
    category_dict = {}
    for name in category:
        category_dict[name] = posts.filter(category=name).count()
    return {'categories': category_dict}