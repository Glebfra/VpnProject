from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)
from rest_framework_simplejwt.authentication import authentication

from .views import RegisterUserAPIView, UserAPIView


app_name = 'users'
urlpatterns = [
    path(r'register/', RegisterUserAPIView.as_view()),
    path(r'account/', UserAPIView.as_view(), name='account_view'),
    path(r'token/', TokenObtainPairView.as_view(), name='user_obtain_token'),
    path(r'refresh/', TokenRefreshView.as_view(), name='user_refresh_token'),
    path(r'verify/', TokenVerifyView.as_view(), name='user_verify_token')
]
