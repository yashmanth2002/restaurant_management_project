from django.db import models

# Create your models here
from django.contrib.auth.models import User

class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('cancelled', "Cancelled"),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'orders')
    order_items = models.ManyToManyField(Menu, related_name='orders')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    Order_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer.username}"
    def calculate_total(self):
        return sum(item.price for item in self.order_items.all())