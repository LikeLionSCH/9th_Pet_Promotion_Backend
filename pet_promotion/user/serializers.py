from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, Pet
from board.models import Post, Comment

# 접속 유저인지 확인
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password= serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Wrong Credentials.")
