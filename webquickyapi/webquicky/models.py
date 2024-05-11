from django.db import models

# Create your models here.

class Product(models.Model):
    productname = models.CharField(max_length=100)
    productdescription1 = models.CharField(max_length=200)
    productdescription2 = models.CharField(max_length=200)
    productnumber = models.IntegerField()
    productimage = models.URLField(max_length=200)
