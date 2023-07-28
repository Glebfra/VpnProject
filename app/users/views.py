from django.contrib.auth.signals import user_logged_in
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer


class RegisterUserAPIView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginUserAPIView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        try:
            user = User.objects.get(email=request.data['email'])
            if user.check_password(request.data['password']):
                user_logged_in.send(sender=user.__class__, request=request, user=user)
                return Response({
                    'name': user.username,
                    'token': user.token
                })
            return Response({
                'error': 'Пользователь не найден'
            })
        except:
            return Response({
                'error': 'Пользователь не найден'
            })
