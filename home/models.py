from django.db import models
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db import models
from django.shortcuts import render
from .models import MenuItem
from django.db import models
from django.db import models
from django.db import models
from django.db import models
from django.db import models
from django.db import models
from django.db import models
from django.db import models
from django.db import models
from django.db import models
from django.db import models
from django.db import models

class NewsItem:
    def __init___(self, title, content, date):
        self.title = title
        self.content = content
        self.date = date

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

class RestaurantInfo(models.Model):
    name = models.CharField(max_length = 200, default="Our Restaurant")
    address = models.TextField()

    def __str__(self):
        return self.name


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

def menu_view(request):
    breadcrumbs = [{'name': 'menu', 'url', ' '}]
    return render(request, 'menu.html', {'breadcrumbs': breadcrumbs})

def order_confirmation_view(request):
    order_number = get_random_string(length=8).upper()
    breadcrumbs = [
        {'name': 'Menu', 'url': reverse('menu')}
        {'name': 'Order Confirmation', 'url': ' '}
    ]
    return render(request, 'order_confirmation.html', {
        'order_number': order_number,
        'breadcrumbs': breadcrumbs
    })

class OpeningHours(models.Model):
    day = models.CharField(max_length=10)

    open_time = models.TimeField()
    close_time = models.TimeField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.day}: {self.open_time} - {self.close_time}

class Chef(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='chef_images/')

    def __str__(self):
        return self.name    

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='menu/')
    alt_text = models.CharField(max_length=255, default='', blank=True)

class RestaurantInfo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name




def menu(request):
    query = request.GET.get('q', '')
    if query:
        items = MenuItem.objects.filter(name__icointains=query)
    else:
        items = MenuItem.objects.all()

    context = {
        'items': item,
        'query': query
    }
    return render(request, 'menu.html', context)

class RestaurantInfo(models.Model):
    name = models.CharField*(max_length=100, default="Our Restaurant")
    address = models.TextField()

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

class RestaurantContact(models.Model):
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"Contact Info - {self.email}"

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ("Appetizer", "Appetizer"),
        ("Main Course", "Main Course"),
        ("Dessert", "Dessert"),
        ("Beverage", "Bevarage"),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="Main Course"
    )

    def __str__(self):
        return f"{self.name} ({self.category})"

class Restaurant(model.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=50, blank=True)

    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class ContactInfo(models.Model):
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"Contact Info ({self.phone})