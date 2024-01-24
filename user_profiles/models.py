from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """
    full_name : Полное имя пользователя.
    email: Email адрес пользователя.
    phone: Мобильный номер пользователя.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile', default=1)
    fullName = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


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


class Avatar(models.Model):
    """
    user: ForeignKey для User модели
    image: ForeignKey для Image модели

    """
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Avatar'
        verbose_name_plural = 'Avatars'
