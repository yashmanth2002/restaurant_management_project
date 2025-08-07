from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer
from django.shortcuts import render
from .models import Restaurant
from restaurant_management.models import Restaurant
from .models restaurant import Restaurant

'''
NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
'''

# Create your views here.
class ItemView(APIView):

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def restaurant_page(request):
            restaurant = Restaurant.objects.first()
            return render(request, 'restaurant.html', {
                'restaurant': restaurant
            })

        def homepage(request):
            restaurant = Restaurant.objects.first()
            return render(request,'home/homepage.html', {'restaurant': restaurant})


def home(request):
    restaurant = Restaurant.objects.first()
    return render(request, 'home.html', {'restaurant': restaurant})
