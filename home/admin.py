from django.contrib import admin
from . models import RestaurantContact
# Register your models here.

class RestaurantContactAdmin(admin.ModelAdmin):
    list_display = ("address", "phone_number", "email")