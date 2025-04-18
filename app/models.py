from django.db import models
from profil.models import CustomUser


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    baza_count = models.IntegerField(default=0)


class Baza(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    t_count = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)


class Test(models.Model):
    baza = models.ForeignKey(Baza, on_delete=models.CASCADE)
    savol = models.TextField()
    a = models.CharField(max_length=200)
    b = models.CharField(max_length=200)
    c = models.CharField(max_length=200)
    d = models.CharField(max_length=200, null=True, blank=True)
    true_var = models.CharField(max_length=1, help_text='Masalan: a')

