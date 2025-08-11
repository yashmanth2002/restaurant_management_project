from django.urls import path
from .views import *
from .views import reservations_view
from .views import home
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path('reservations/', reservations_view, name='reservations')
    path('', home, name='home'),
    path('', home, name='home')
    path('order/', views.place_order_view, name='place_order')
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('privacy-policy/', privacy_policy_view, name='privacy_policy'),
]