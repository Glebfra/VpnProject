from django.contrib.auth.signals import user_logged_in
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import UserSerializer


class RegisterUserAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginUserAPIView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        user = User.objects.get(**request.data)
        if user:
            try:
                refresh = RefreshToken.for_user(user)
                user_details = {
                    'name': user.username,
                    'token': str(refresh.access_token)
                }
                user_logged_in.send(sender=user.__class__, request=request, user=user)
                return Response(user_details)
            except Exception as e:
                raise e
        else:
            res = {
                'error': 'Cannot authenticate with the given credentials or the account has been deactivated'
            }
            return Response(res)
