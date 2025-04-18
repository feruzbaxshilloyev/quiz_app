from django.db import models
from profil.models import CustomUser

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    test_count = models.IntegerField(default=0)


class Test(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)