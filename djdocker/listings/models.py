from django.db import models

# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length =250)
    price = models.IntegerField()
    num_bedroom =models.IntegerField()
    num_bathroom = models.IntegerField()
    square_meter = models.IntegerField()
    address = models.CharField(max_length =150)
    image = models.ImageField()
    aircode = models.CharField(max_length =50)


def __str__(self):
    return self.title