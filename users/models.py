from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
