import jwt
from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        return attrs

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
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
