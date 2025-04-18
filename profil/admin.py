from django.contrib import admin
from .models import CustomUser


# Register your models here.

class CustomUserAdmin(CustomUser):
    fields = []


admin.site.register(CustomUser, CustomUserAdmin)
