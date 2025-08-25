from django.contrib import admin
from . models import RestaurantContact
# Register your models here.
from django.contrib import admin
from .models import ContactInfo
from django.contrib import admin
from . models import RestaurantReview
from django.contrib import admin
from .models import RestaurantInfo

class RestaurantContactAdmin(admin.ModelAdmin):
    list_display = ("address", "phone_number", "email")
    list_display = ("phone", "email", "address")
    list_display = ("user", "rating", "created_at")
    search_fields = ("user_username", "comment")
    list_filter = ("rating", "craeted_at")
    admin.site.register(RestaurantInfo)