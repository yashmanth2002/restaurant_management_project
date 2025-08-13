from .models import RestaurantInfo
import datetime


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