from .models import RestaurantInfo

def restaurant_info(request):
    try:
        info = RestaurantInfo.objects.first()
    except RestaurantInfo.DoesNotExist:
        info = None
    return {'restaurant_info': info}