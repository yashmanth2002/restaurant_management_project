from django.urls import path
from .views import *
from .views import reservations_view

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path('reservations/', reservations_view, name='reservations')
]