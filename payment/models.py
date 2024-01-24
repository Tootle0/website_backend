from django.db import models


class Payment(models.Model):
    card_number = models.CharField(max_length=255, default='9999999999999999')
    name = models.CharField(max_length=255, default='Celery Ananasov')
    month = models.CharField(max_length=2, default='12')
    year = models.CharField(max_length=4, default='2025')
    code = models.CharField(max_length=3, default='001')
    payment_type = models.CharField(max_length=255, default='Онлайн картой')
