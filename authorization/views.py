import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.decorators import parser_classes
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LoginSerializer


class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=json.loads(request.body))
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            return Response({'success': True}, status=200)

        else:
            return Response({'Error': 'Invalid username or password'}, status=500)


class SignupView(APIView):
    @parser_classes([MultiPartParser])
    def post(self, request):
        # data = json.loads(request.body)

        name = request.data.get('name')
        username = request.data.get('username')
        password = request.data.get('password')

        if not name and False:
            raise ValidationError({'name': 'Name is required'})
        if not username:
            raise ValidationError({'username': 'Username is required'})
        if not password:
            raise ValidationError({'password': 'Password is required'})

        user = User.objects.create_user(
            first_name=name,
            username=username,
            password=password,
        )

        user.save()

        return JsonResponse({'success': True}, status=200)


class SignOutView(APIView):

    def post(self, request):

        logout(request)

        return Response({'success': True}, status=200)

