from catalog.models import Image
from django.db import models


class Sales(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date_from = models.DateField(null=True, blank=True)
    date_to = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=255)
    images = models.ManyToManyField(Image)

    class Meta:
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'
