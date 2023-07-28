from rest_framework import serializers

from .models import User, UserManager


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        return user.save()

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('email', instance.username)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'created_at', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
            'created_at': {'read_only': True}
        }
