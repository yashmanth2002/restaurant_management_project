from django.urls import path
from .views import menu_view
from .views import home
from . import views

urlpatterns = [
    path('contact/', contact_page, name='contact'),
    path('', home, name='home'),
    path('about/', views.about_page, name='about')
]