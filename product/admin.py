from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'images')


admin.site.register(Product, ProductAdmin)
