from rest_framework import serializers

from .models import Sales


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ('id', 'price', 'sale_price', 'date_from', 'date_to', 'title', 'images')
