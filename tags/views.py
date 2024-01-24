
from django.shortcuts import render
from .serializers import TagSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Tag


@api_view(['GET'])
def get_tags(request):

    tags = Tag.objects.all()

    tags_serializer = TagSerializer(tags, many = True)
    
    return Response(tags_serializer.data)