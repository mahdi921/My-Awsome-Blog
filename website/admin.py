from django.contrib import admin
from website.models import Newsletter

# Register your models here.
@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_date')
    list_filter = ('created_date',)
    search_fields = ('email',)
    date_hierarchy = 'created_date'