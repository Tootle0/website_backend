from django.contrib.auth import get_user, get_user_model
from django.db import models
from product.models import Product


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



class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Basket(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    count = models.IntegerField()
    date = models.DateField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    freeDeliver = models.BooleanField()
    images = models.ManyToManyField(Image)
    tags = models.ManyToManyField(Tag)
    reviews = models.IntegerField()
    rating = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


def get_current_user(request=None):
    if request:
        user = get_user(request)
        if user.is_authenticated:
            return user
    return None


class BasketItem(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=get_current_user)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='basket_items')
    count = models.IntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    class Meta:
        verbose_name = 'Basket Item'
        verbose_name_plural = 'Basket Items'
