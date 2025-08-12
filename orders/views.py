from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.shortcuts import render
from datetime import datetime
from django.shortcuts import render
from .models import MenuItem
from .models import TodaySpecial
from django.utils.timeZone import now
from django.shortcuts import render
from .models import RestaurantInfo


class MenuAPIView(APIView):
    def get(self, request):
        menu = [
            {"name": "Spaghetti Carbonara", "description": "Classic Italian pasta with creamy sauce and pancetta.", "price": 12.99},
            {"name": "Margherita Pizza", "description": "Traditional pizza with tomato, mozzarella, and basil.", "price": 10.99},
            {"name": "Caesar Salad", "description": "Romaine letuce with Caesar dressing, croutons, and parmesan.", "price": 8.99},
        ]

        return Response(menu, status=status.HTTP_200_OK)

    def menu_preview(request):

        menu_items = [
            {'name': 'Paneer Tikka', 'price': 240},
            {'name': 'Chicken Biryani', 'price': 320},
            {'name': 'Masala Dosa', 'price': 180},
            {'name': 'Gulab Jamun', 'price': 90},
        ]
        return render(request, 'menu_preview.html', {'menu_items': menu_items})

    def homepage_view(request):
        return render(request, 'home/homepage.html', {
            'restaurant_name': 'Spice Garden'
        })

    def reservations_view(request):
        return render(request, 'Reservations.html')

    def your_view(request):
        context = {
            'current_year': datetime.now().year,
        }
        return render(request, 'your_template.html', context)

    def menu_view(request):
        menu_items = MenuItem.objects.all()
        return render(request, 'menu.html', {'menu_items': menu_items})

        def home(request):
            restaurant = Restaurant.objects.first()
            return render(request, 'home.html', {'restaurant': restaurant})

def home_view(request):
    today = now().date()
    specials = TodaySpecial.objects.filter(created_at=today)
    breadcrumbs = []
    return render(request, 'restaurant_home.html', {
        'specials': specials,
        'breadcrumbs': breadcrumbs
    })

def contact_view(request):
    info = RestaurantInfo.objects.first()
    return render(request, 'contact.html', {'restaurant_info': info})

