from django.db import models
from user.models import User
# Create your models here.

class Images(models.Model):
    photo = models.ImageField(upload_to='images')

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now_add=True)
    image = models.ForeignKey(Images, blank=False, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, db_column="user_id")

class Comment(models.Model):
    comment = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Post, blank=False, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, db_column="user_id")