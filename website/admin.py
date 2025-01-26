from django.contrib import admin
from website.models import Newsletter, Contact

# Register your models here.
@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_date')
    list_filter = ('created_date',)
    search_fields = ('email',)
    date_hierarchy = 'created_date'


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_date')
    list_filter = ('created_date',)
    search_fields = ('name', 'email', 'subject')
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
