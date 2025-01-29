from django.contrib.sitemaps import Sitemap
from blog.models import Post
from django.utils import timezone

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.filter(published_date__lte=timezone.now(), status=1)

    def lastmod(self, obj):
        return obj.updated_date