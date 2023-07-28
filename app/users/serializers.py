import jwt
from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=128, min_length=8)

    def validate(self, attrs):
        username = attrs.get('username', None)
        email = attrs.get('email', None)

        token = attrs.get('token', None)
        if token is None:
            raise serializers.ValidationError('Токен не может быть пустым')

        user = User.objects.get_user_by_token(token=token)
        if user is None:
            raise serializers.ValidationError('Пользователь не найден')

        return {
            'username': user.username,
            'email': user.email,
            'token': token
        }

    @staticmethod
    def get_user(token) -> User:
        if token is None:
            raise serializers.ValidationError('Токен не может быть пустым')

        user = User.objects.get_user_by_token(token=token)
        if user is None:
            raise serializers.ValidationError('Пользователь не найден')
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('email', 'username', 'token')
        extra_kwargs = {
            'email': {'read_only': True},
            'username': {'read_only': True}
        }


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['password', 'username', 'token']

    def validate(self, attrs):
        username = attrs.get('username', None)
        password = attrs.get('password', None)

        if username is None:
            raise serializers.ValidationError('Имя пользователя не может быть пустым')
        if password is None:
            raise serializers.ValidationError('Пароль не может быть пустым')

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError('Пользователь не найден')
        if not user.is_active:
            raise serializers.ValidationError('Пользователь не активен')

        return {
            'username': user.username,
            'token': user.token
        }


class RegistrationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'token']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        username = attrs.get('username', None)
        password = attrs.get('password', None)
        email = attrs.get('email', None)

        if username is None:
            raise serializers.ValidationError('Имя пользователя не может быть пустым')
        if email is None:
            raise serializers.ValidationError('Адрес электронной почты не может быть пустым')
        if password is None:
            raise serializers.ValidationError('Пароль не может быть пустым')

        return {
            'username': username,
            'password': password,
            'email': email
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
