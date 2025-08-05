from django.db import models

# Create your models here
from django.contrib.auth.models import User
from django.contrib import admin
from .models import menu, Order


admin.site.register(Menu)
admin.site.register(Order)

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'total_amount', 'order_status', 'created_at')
    list_filter = ('order_status', 'created_at')
    search_fields = ('customer__username', )

admin.site.register(Menu, MenuAdmin)
admin.site.register(Order, OrderAdmin)

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