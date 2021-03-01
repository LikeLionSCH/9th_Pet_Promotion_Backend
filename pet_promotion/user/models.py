from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Pet(models.Model):
    user = models.ForeignKey("User", related_name="user", on_delete=models.CASCADE, db_column="user_id")
    birth = models.DateField()
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/%Y/%m/%d")
