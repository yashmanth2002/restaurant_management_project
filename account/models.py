from django.db import models
from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)

class RestaurantInfo(models.Model):
    name = models.CharField(max_length=200, default="Our Restaurant")
    address = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name