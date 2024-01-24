from basket.models import BasketItem
from rest_framework import serializers


class BasketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItem
        fields = ['id', 'count', 'total_cost']
