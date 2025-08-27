from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date', 'time', 'guests', 'created_at')
    list_filter = ('date', 'time')
    search_fields = ('name', 'email')