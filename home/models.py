from django.db import models
from django.db import models
# Create your models here.
class Contact(models.Model):
    name = models.Charfield(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.Charfield(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class RestaurantLocation(models.Model):
    addrss = models.Charfield(max_length=255)
    city = models.Charfield(max_length=100)
    state = models.Charfield(max_length=100)
    zip_code = models.Charfield(max_length=10)

    def __str__(self):
        return f"{self.address}, {self.city}, {self.state}, {self.zip_code}"