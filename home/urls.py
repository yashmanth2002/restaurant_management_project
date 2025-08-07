from django.urls import path
from .views import menu_view
from .views import home

urlpatterns = [
    path('contact/', contact_page, name='contact'),
    path('', home, name='home')
]