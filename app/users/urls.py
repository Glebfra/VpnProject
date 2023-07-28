from django.urls import path

from .views import RegisterUserAPIView, LoginUserAPIView, UserAPIView

app_name = 'users'
urlpatterns = [
    path(r'register/', RegisterUserAPIView.as_view()),
    path(r'login/', LoginUserAPIView.as_view()),
    path(r'account/', UserAPIView.as_view())
]
