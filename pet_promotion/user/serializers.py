from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import User, Pet
from board.models import Post, Comment

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'password',
        )