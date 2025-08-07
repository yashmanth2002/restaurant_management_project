from django.urls import path
from .views import MenuAPIView
from .views import menu_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('preview-menu/', menu_preview, name='menu-provider'),
    path('menu/', menu_view, name='menu'),
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
]