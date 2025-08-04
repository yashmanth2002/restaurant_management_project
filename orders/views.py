from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MenuAPIView(APIView):
    def get(self, request):
        menu = [
            {"name": "Spaghetti Carbonara", "description": "Classic Italian pasta with creamy sauce and pancetta.", "price": 12.99},
            {"name": "Margherita Pizza", "description": "Traditional pizza with tomato, mozzarella, and basil.", "price": 10.99},
            {"name": "Caesar Salad", "description": "Romaine letuce with Caesar dressing, croutons, and parmesan.", "price": 8.99},
        ]

        return Response(menu, status=status.HTTP_200_OK)