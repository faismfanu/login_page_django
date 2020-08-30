from django.db import models

# Create your models here.

class User:
    username = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    password = models.CharField(max_length=225)

    

class Product(models.Model):
    name = models.CharField(max_length=225)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
