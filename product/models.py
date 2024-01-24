from django.db import models

from tags.models import Tag
from catalog.models import Category

class Image(models.Model):
    """
    src: URL изображения
    alt: Альтернативный текст для изображения.

    """
    src = models.CharField(max_length=255)
    alt = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2,null=False)
    count = models.IntegerField()
    date = models.DateTimeField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    freeDelivery = models.BooleanField()
    images = models.ImageField(Image, null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    reviews = models.IntegerField()
    rating = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
