from django.db import models

class Restaurant(models.model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    image = models.ImageField(upload_to= 'menu_images/', blank=True, null=True)

    def __str__(self):
        return self.name