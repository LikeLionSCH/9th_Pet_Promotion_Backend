from django.db import models

# Create your models here.

class Comment(models.Model):
    comment = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Post, blank=False, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey("user.User", related_name="user", on_delete=models.CASCADE, db_column="user_id")