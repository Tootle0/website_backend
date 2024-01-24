from django.db import models


class Image(models.Model):
    src = models.CharField(max_length=255)
    alt = models.CharField(max_length=255)
    image = models.FileField(upload_to='media/')

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'


class Subcategory(models.Model):
    title = models.CharField(max_length=255)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'


class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)
    subcategories = models.ManyToManyField(Subcategory)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    subcategories = models.ManyToManyField(Subcategory)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
