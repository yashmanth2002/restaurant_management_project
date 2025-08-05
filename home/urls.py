from django.urls import path
from .views import menu_view

urlpatterns = [
    path('contact/', contact_page, name='contact'),
]