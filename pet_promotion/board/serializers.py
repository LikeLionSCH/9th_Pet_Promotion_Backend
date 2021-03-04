from rest_framework import serializers
from .models import Images, Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'create_date', 'update_date', 'image', 'user')


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'create_date', 'update_date', 'image', 'user')


class PostPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'create_date', 'update_date', 'image', 'user')