from django.shortcuts import render
from .models import Restaurant
from django.db import models
from django.shortcuts import render
from .models import RestaurantInfo
from django.shortcuts import render
from .models import RestaurantInfo

# Create your views here.

def homepage(request):
    restaurant = Restaurant.objects.first()

    context = {
        'restaurant_name': restaurant.name if restaurant else 'Your Restaurant'
    }
    return render(request, 'home.html', context)

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

def about_us_view(request):
    info = RestaurantInfo.objects.first()
    return render(request, 'about_us.html', {'info': info})

def contact_us(request):
    restaurant_info = RestaurantInfo.objects.first()
    return render(request, 'home/contact.html', {'restaurant_info': restaurant_info})