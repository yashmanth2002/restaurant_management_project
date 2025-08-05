from django.urls import path
from .views import MenuAPIView

urlpatterns = [
    path('preview-menu/', menu_preview, name='menu-provider'),
]