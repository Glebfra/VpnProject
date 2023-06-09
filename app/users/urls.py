from django.urls import path, re_path, include
from .views import RegisterUserAPIView, LoginUserAPIView


urlpatterns = [
    path(r'register/', RegisterUserAPIView.as_view()),
    path(r'login/', LoginUserAPIView.as_view())
]
