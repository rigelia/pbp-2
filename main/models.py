from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.IntegerField()
    description = models.TextField()
    effects = models.TextField(default="No effects")

