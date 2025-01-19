from django.urls import path, re_path
from blog.views import index_view, about_view, contact_view, blog_single_view, blog_view

app_name = 'blog'

urlpatterns = [
    path('', index_view, name='index'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('blog/', blog_view, name='blog'),
    path('<int:pid>', blog_single_view, name='single'),
]