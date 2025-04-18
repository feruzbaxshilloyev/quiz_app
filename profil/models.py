from django.db import models

# Create your models here.


class CustomUser(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField()

