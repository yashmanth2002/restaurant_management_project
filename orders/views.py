from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render

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