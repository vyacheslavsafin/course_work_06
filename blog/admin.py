from django.contrib import admin

from blog.models import Blog
from pytils.translit import slugify


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    fields = ('title', 'content', 'preview',)
    search_fields = ('title', 'content',)

    def save_model(self, request, obj, form, change):
        obj.slug = obj.slug = slugify(obj.title)
        super().save_model(request, obj, form, change)
