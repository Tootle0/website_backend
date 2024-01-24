from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Sales
from .serializers import SalesSerializer


@api_view(['GET'])
def get_sales(request):
    sales = Sales.objects.all()

    sales_serializer = SalesSerializer(sales, many=True)

    return JsonResponse({'data': sales_serializer.data})
