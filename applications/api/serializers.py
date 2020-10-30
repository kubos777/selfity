from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from .models import Test, User

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('name',)

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('telephone', 'password')
        extra_kwargs = {'password': {'write_only': True}, }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserSerializer(serializers.ModelSerializer):   
    class Meta:
        model = User
        fields = ('id', 'telephone', )

class UserTelephoneSerializer(serializers.ModelSerializer):   
    class Meta:
        model = User
        fields = ('telephone', )
