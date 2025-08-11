from django.db import settings

def restaurant_info(request):
    return{
        'restaurant_phone': settings.RESTAURANT_PHONE
    }