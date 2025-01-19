from django.urls import path
from blog.views import index_view, about_view, contact_view#, blog_single_view

app_name = 'blog'

urlpatterns = [
    path('', index_view, name='index'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    # path('blog/<int:pid>', blog_single_view, name='single'),
]