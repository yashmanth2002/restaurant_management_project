from django.contrib import admin
from . models import RestaurantContact
# Register your models here.
from django.contrib import admin
from .models import ContactInfo
from django.contrib import admin
from . models import RestaurantReview
from django.contrib import admin
from .models import RestaurantInfo
from django.contrib import admin
from .models import TermsOfService
from django.contrib import admin
from .models import FAQ
from django.contrib import admin
from .models import RestaurantInfo


@admin.register(RestaurantInfo)
class RestaurantInfoAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number")


@admin.register(FAQ)
class FAQ@Admin(admin.ModelAdmin):
    list_display = ("question")

class RestaurantContactAdmin(admin.ModelAdmin):
    list_display = ("address", "phone_number", "email")
    list_display = ("phone", "email", "address")
    list_display = ("user", "rating", "created_at")
    search_fields = ("user_username", "comment")
    list_filter = ("rating", "craeted_at")
    admin.site.register(RestaurantInfo)
    admin.site.register(TermsOfService)