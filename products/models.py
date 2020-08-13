from django.db import models

# Create your models here.
class Product(models.Model):
    Name = models.CharField()
    price =models.IntegerField()

