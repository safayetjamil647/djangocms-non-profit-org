from django.contrib import admin

# Register your models here.

from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'blog_desc')
    search_fields = ['blog_title', 'blog_desc']

admin.site.register(Blog, BlogAdmin)
