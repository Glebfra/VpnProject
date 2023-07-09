from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return User(**validated_data).save()

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
