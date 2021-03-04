from django.urls import path
from .views import *

urlpatterns = [
    path('post/<int:post_id>/comments/', views.comment_create),
    path('post/<int:post_id>/comments/<int:comment_id>/', views.comment_update_and_delete),
]
