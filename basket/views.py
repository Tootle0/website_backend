from django.http import JsonResponse
from django.views import View
from product.models import Product
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.views import APIView
from django.http import HttpRequest
from .models import Basket, BasketItem
from .serializers import BasketItemSerializer


class BasketView(APIView):

    def get(self, request: Request, *args, **kwargs):
        user = request.user  # Получение текущего юзера
        basket_items = BasketItem.objects.filter(user=request.user)  # Фильтрация продуктов в корзине для текущего юзера

        json_basket_items = []

        # Итерируется по продуктам и конвертирует их в JSON объект
        for basket_item in basket_items:
            product = basket_item.product
            json_basket_item = {
                "id": product.id,
                "price": product.price,
                "count": basket_item.count,
                "date": product.date,
                "title": product.title,
                "description": product.description,
                "freeDelivery": product.freeDelivery,
                "images": product.images.url if product.images else None,
                "tags": [tag.name for tag in product.tags.all()],
                "reviews": product.reviews,
                "rating": product.rating,
            }
            json_basket_items.append(json_basket_item)

        # Возвращает JsonResponse
        return JsonResponse(json_basket_items, safe=False)

    def post(self, request: Request, *args, **kwargs):
        serializer = BasketItemSerializer(data=request.data)  # Создание сериализатора для данных корзины

        if serializer.is_valid():  # Если сериализатор валиден, то сохранить
            product_id = request.data.get('id')

            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return JsonResponse({'error': 'Product not found'}, status=400)

            validated_data = serializer.validated_data
            basket_item = BasketItem(product=product, count=validated_data['count'], user=request.user)

            basket_item.total_cost = basket_item.count * product.price
            basket_item.save()

            return JsonResponse({
                'id': basket_item.id,
                'count': basket_item.count,
                'total_cost': basket_item.total_cost
            })
        else:
            return JsonResponse(serializer.errors, status=400)

    def delete(self, request: Request, *args, **kwargs):
        """Удаление из корзины"""
        """TODO: Fix Delete/Addition Function"""
        # Получение ID

        product_id = request.data.get('id')
        # Получение объекта
        basket_item = Basket.objects.get(id=product_id)
        # Удаление
        basket_item.delete()
        # Получение всех продуктов связанных с пользователем
        basket_items = Basket.objects.filter(user=request.user)

        # Конвертация объектов в JSON
        json_basket_items = []
        for basket_item in basket_items:
            json_basket_item = {
                "price": basket_item.price,
                "count": basket_item.count,
                "date": basket_item.date,
                "title": basket_item.title,
                "description": basket_item.description,
                "freeDelivery": basket_item.freeDelivery,
                "images": [image.src for image in basket_item.images.all()],
                "tags": [tag.name for tag in basket_item.tags.all()],
                "reviews": basket_item.reviews,
                "rating": basket_item.rating,
            }
            json_basket_items.append(json_basket_item)

        # Возвращение JSON
        return JsonResponse(json_basket_items, safe=False)
