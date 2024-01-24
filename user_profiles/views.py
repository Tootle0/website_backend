from django.core.files.uploadedfile import SimpleUploadedFile
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User

from .models import Profile
from .serializers import ProfileSerializer


class ProfileView(APIView):
    def get(self, request):
        profile, created = Profile.objects.get_or_create(user=request.user)
        serializer = ProfileSerializer(profile)
        return JsonResponse(serializer.data)

    def post(self, request):
        profile, created = Profile.objects.get_or_create(user=request.user)
        serializer = ProfileSerializer(profile, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PostProfilePasswordView(APIView):
    def post(self, request):
        user = request.user

        if not user.check_password(request.data['current_password']):
            return JsonResponse({'error': 'Current Password in incorrect'}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(request.data['new_password'])

        user.save()

        return JsonResponse({'success': 'Password has been updated successfully'})


class PostProfileAvatarView(APIView):
    def post(self, request):
        user = request.user

        avatar_file = request.FILES.get('avatar')

        if not hasattr(user, 'profile'):
            profile = Profile.objects.create(user=user)
        else:
            profile = user.profile

        if avatar_file:
            avatar_in_memory = SimpleUploadedFile(
                name=avatar_file.name,
                content=avatar_file.read(),
                content_type=avatar_file.content_type
            )

            profile.avatar = avatar_in_memory

            profile.save()
        return JsonResponse({'success': 'Avatar has been uploaded successfully'})
