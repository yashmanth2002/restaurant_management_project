from django.urls import path
from .views import *
from .views import reservations_view
from .views import home

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path('reservations/', reservations_view, name='reservations')
    path('', home, name='home'),
]