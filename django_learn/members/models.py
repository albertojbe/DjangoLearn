from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=55)
    description = models.CharField(max_length=255)
    pricec = models.FloatField(255)
