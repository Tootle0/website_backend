from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .models import Product
from .serializers import ProductSerializer


@api_view(['GET'])
def get_popular_products(request):
    # Получение всех популярный продуктов
    products = Product.objects.order_by('-count')

    # Сериализация
    products_serializer = ProductSerializer(products, many=True)

    return Response(products_serializer.data)


@api_view(['GET'])
def get_limited_products(request):
    # Получение продуктов которых 10 или меньше
    products = Product.objects.filter(count__lte=10)

    products_serializer = ProductSerializer(products, many=True)

    return Response(products_serializer.data)


@api_view(['GET'])
def get_product(request, pk):
    product = Product.objects.get(pk=pk)

    product_serialize = ProductSerializer(product, many=False)

    return Response(product_serialize.data)
