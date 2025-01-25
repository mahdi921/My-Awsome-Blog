from django.contrib import admin
from blog.models import Post, Category, Comment

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'counted_views', 'status',
                    'published_date', 'created_date', 'updated_date')
    list_filter = ('status', 'created_date')
    search_fields = ('title', 'author', 'content')
    actions = ['make_published']
    empty_value_display = '-empty-'
    date_hierarchy = 'created_date'

admin.site.register(Category)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'approved', 'created_date', 'updated_date')
    list_filter = ('approved', 'created_date',)
    search_fields = ('name','email', 'message')
    actions = ['approve_comments']
    empty_value_display = '-empty-'
    date_hierarchy = 'updated_date'