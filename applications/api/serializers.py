from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from .models import Test, User, Image
from django.core.files.base import ContentFile
import base64
import uuid
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
    telephone = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8)
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['telephone'], validated_data['password'])
        return user   
    class Meta:
        model = User
        fields = ('id', 'telephone','password' )

class UserTelephoneSerializer(serializers.ModelSerializer):   
    class Meta:
        model = User
        fields = ('telephone', )

class ImageSerializer(serializers.Serializer):
    thumbnail = serializers.ImageField()
    created_at = serializers.DateTimeField()
    hashtag = serializers.CharField()
    coords = serializers.CharField()

class ImagesSerializer(serializers.Serializer):
    file = serializers.ImageField()

class HashtagSerializer(serializers.Serializer):
    hashtag = serializers.CharField()



