from django.db import models
from django.db import models
from django.db import models
from django.contrib.auth.models import User
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

class Item(models.Model):
    name = models.Charfield(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, through=CartItem)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    Item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)