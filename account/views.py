from django.shortcuts import render
from .models import Restaurant
# Create your views here.

def homepage(request):
    restaurant = Restaurant.objects.first()

    context = {
        'restaurant_name': restaurant.name if restaurant else 'Your Restaurant'
    }
    return render(request, 'home.html', context)