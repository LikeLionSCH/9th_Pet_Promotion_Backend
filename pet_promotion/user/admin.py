from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Pet


# Register your models here.
admin.site.register(Pet)

@admin.register(User)
class AdminUser(UserAdmin):
    model = User

    fieldsets = (
        (None, {"fields": ("username", "email", "password")},),
    )
    
    list_display = ['username', 'email', 'password']
