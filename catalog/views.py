from django.core.paginator import Paginator, EmptyPage
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


@api_view(['GET'])
def product_catalog_view(request):
    # Получение параметров
    filter_name = request.GET.get('filter_name')
    filter_value = request.GET.get('filter_value')
    subcategories = request.GET.getlist('subcategories')
    sort_by = request.GET.get('sort_by')
    sort_order = request.GET.get('sort_order')
    page = request.GET.get('page', 1)
    per_page = request.GET.get('per_page', 10)

    # Фильтрация
    products = Product.objects.all()

    if filter_name and filter_value:
        filter_kwargs = {f'{filter_name}__icontains': filter_value}
        products = products.filter(**filter_kwargs)

    # Фильтрация по саб-категорий если указано
    if subcategories:
        products = products.filter(subcategories__in=subcategories)

    # Сортировка
    if sort_by and sort_order:
        ordering_field = f'{sort_by}'
        if sort_order.lower() == 'desc':
            ordering_field = f'-{ordering_field}'

        products = products.order_by(ordering_field)

    # Пагинация
    paginator = Paginator(products, per_page)
    try:
        page_obj = paginator.page(page)
    except EmptyPage:
        return Response({
            'error': 'Invalid page number',
        }, status=400)


        # Сериализация
    products_serializer = ProductSerializer(page_obj.object_list, many=True)

    # Возвращение JSON
    return Response({
        'products': products_serializer.data,
        'count': paginator.count,
        'next': page_obj.next_page_number() if page_obj.has_next() else None,
        'previous': page_obj.previous_page_number() if page_obj.has_previous() else None,
    })

@api_view(['GET'])
def get_categories(request):
     # Получение всех категорий
    categories = Category.objects.all()

    # Сериализация категорий
    categories_serializer = CategorySerializer(categories, many=True)

    return Response(categories_serializer.data)
