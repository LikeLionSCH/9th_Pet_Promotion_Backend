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
)

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ['get', 'post']


class PostCreateViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    http_method_names = ['get', 'post']


class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostPutSerializer
    lookup_field = 'id'


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'



