from .models import RestaurantInfo
import datetime
from django.conf import settings


def restaurant_info(request):
    try:
        info = RestaurantInfo.objects.first()
    except RestaurantInfo.DoesNotExist:
        info = None
    return {'restaurant_info': info}


def current_year(request):
    return{
        'current_year': datetime.date.today().year
    }

def restaurant_address(request):
    return {
        'RESTAURANT_ADDRESS': settings.RESTAURANT_ADDRESS
    }