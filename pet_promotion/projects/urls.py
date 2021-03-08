"""projects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from board.views import (
    PostUpdateAPIView, PostDeleteAPIView, PostViewSet ,PostCreateViewSet, CommentUpdateAPIView, CommentDeleteAPIView, CommentViewSet, CommentCreateViewSet
)

router = routers.DefaultRouter()
router.register('post', PostViewSet, basename='post')
router.register('post-create', PostCreateViewSet, basename='post_create')
router.register('comment', CommentViewSet, basename='comment')
router.register('comment-create', CommentCreateViewSet, basename='comment_create')

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    url('api/post/(?P<id>[\w-]+)/edit/$', PostUpdateAPIView.as_view(), name='post_update'),
    url('api/post/(?P<id>[\w-]+)/delete/$', PostDeleteAPIView.as_view(), name='post_delete'),
    url('api/comment/(?P<id>[\w-]+)/edit/$', CommentUpdateAPIView.as_view(), name='comment_update'),
    url('api/comment/(?P<id>[\w-]+)/delete/$', CommentDeleteAPIView.as_view(), name='comment_delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

