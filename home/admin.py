from django.contrib import admin
from . models import RestaurantContact
# Register your models here.
from django.contrib import admin
from .models import ContactInfo

class RestaurantContactAdmin(admin.ModelAdmin):
    list_display = ("address", "phone_number", "email")
    list_display = ("phone", "email", "address")