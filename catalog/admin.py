from django.contrib import admin

from .models import Category, Subcategory, Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('src', 'alt', 'image')


admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Image)
