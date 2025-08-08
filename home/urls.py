from django.urls import path
from .views import menu_view
from .views import home
from . import views
from django.conf.urls.static import static 

urlpatterns = [
    path('contact/', contact_page, name='contact'),
    path('', home, name='home'),
    path('about/', views.about_page, name='about')
    path('contact/', contact_page, name='contact'),
    path('', home, name='home'),
    path('about', views.about_page, name='about'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)