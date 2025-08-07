from django.urls import path
from .views import MenuAPIView
from .views import menu_view

urlpatterns = [
    path('preview-menu/', menu_preview, name='menu-provider'),
    path('menu/', menu_view, name='menu'),
]