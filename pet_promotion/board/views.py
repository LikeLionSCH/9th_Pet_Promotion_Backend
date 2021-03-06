from rest_framework import permissions
from .models import Images, Post, Comment
from rest_framework.generics import (
    ListCreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from rest_framework.viewsets import ModelViewSet
from .serializers import (
    PostSerializer,
    PostCreateSerializer,
    PostPutSerializer,
    CommentSerializer,
    CommentCreateSerializer,
    CommentPutSerializer,
)

class PostViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ['get', 'post']

class PostCreateViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    http_method_names = ['get', 'post']

class PostUpdateAPIView(UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostPutSerializer
    lookup_field = 'id'

class PostDeleteAPIView(DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    http_method_names = ['get', 'post']

class CommentCreateViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    http_method_names = ['get', 'post']

class CommentUpdateAPIView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentPutSerializer
    lookup_field = 'id'

class CommentDeleteAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'