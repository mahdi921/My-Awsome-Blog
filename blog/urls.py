from django.urls import path
from blog.views import blog_single_view, blog_view#, search_view

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='blog'),
    path('<int:pid>/', blog_single_view, name='single'),
    path('search/', blog_view, name='search'),
]