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
    baza = models.ForeignKey(Baza, on_delete=models.CASCADE, related_name='test_set')
    savol = models.CharField(max_length=255)
    image = models.ImageField(upload_to='test_images/', null=True, blank=True)
    a = models.TextField()
    b = models.TextField()
    c = models.TextField()
    d = models.TextField(null=True, blank=True)
    times = models.IntegerField(help_text="Savolni ishlash uchun vaqt", default=60)
    true_var = models.CharField(max_length=1, choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')])

    def __str__(self):
        return self.savol

