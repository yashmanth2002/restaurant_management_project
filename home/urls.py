from django.urls import path
from .views import menu_view
from .views import home
from . import views
from django.conf.urls.static import static 
from .views import submit_feedback
from django.urls import path
from .views import contact_view, thank_you_view
from django.urls import path
from . import views
from django.urls import path
from . import views
from django.urls import path
from . import views
from django.urls import path
from .import views
from django.urls import path
from . import views
from django.conf.urls import handler403
from your_app import views
from django.urls import path
from .import views
from django.urls import path
from . import views
from django.urls import path
from . import views
from django.urls import path
from . import views
from django.urls import path
from . import views
from django.urls import path
from . import views
from django.urls import path
from . import views
from django.urls import path
from . import views
from django.urls import path
from . import views
from django.urls import path
from home import views
from django.urls import path
from . import views
from django.urls import path
from . import views
from django.urls import path
from . import views
from django.urls import path
from . import views
from django.urls import path
from . import views
from django.urls import path
from . import views
from django.urls import path
from . import views
from django.urls import path
from . import views
from django.urls import path
from . import views
from django.urls import path
from . import views
from django.urls import path
from . import views


urlpatterns = [
    path('contact/', contact_page, name='contact'),
    path('', home, name='home'),
    path('about/', views.about_page, name='about')
    path('contact/', contact_page, name='contact'),
    path('', home, name='home'),
    path('about', views.about_page, name='about'),
    path('feedback/', submit_feedback, name='submit_feedback')
    path('contact/', contact_view, name='contact')
    path('contact/thank-you/', thank_you_view, name='thank_you')
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    path('about/', views.about, name='about')
    path('', views.homepage, name='home'),
    path('', views.home, name='home'),
    path('reservations/', views.reservations, name='reservations')
    path('menu/', views.menu, name='menu')
    path('reservations/', views.reservations, name='reservations')
    path('privacy-policy/', views.privacy-policy, name="privacy-policy")
    path('gallery/', views.gallery, name='gallery'),
    path('location/', views.location_page, name='location'),
    path('reservation/', views.reservation_page, name='reservation'),
    path('menu/', views.menu_page, name='menu'),
    path('', views.home, name='home')
    path('menu/', views.menu,name='menu')
    path('about/', views.about, name='about')
    path('contact/', views.contact, name='contact')
    path('menu/', views.menu, name='menu'),
    path('add-to-cart/<int:item_id>/'), views.add_to_cart, name='add_to_cart'),
    path('menu/', views.menu, name='menu'),
    path('add-to-cart/<int:item_id', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_port'),
    path('', views.home, name='home'),
    path('reservations/', views.reservations, name='reservations'),
    path('', views.home_view, name='home')
    path('cart/', views.cart_view, name='cart')
    path('', views.home_view, name='home')
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('gallery/', views.gallery, name='gallery'),
    path('about/', views.about, name='about'),
    path('cart/', view.cart, name='cart'),
    path('cart/', views.cart, name='cart'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    path("privacy/", views.privacy_policy, name="privacy_policy")
    path('privacy-policy/', views.privacy_policy, name="privacy_policy"),
    path('locations/', views.locations, name='location'),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),
    path("privacy/", views.privacy_policy, name="privacy"),
    path("contact/", views.contact_view, name="contact"),
    path("news?", views.news_list, name="news")


    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = view.custom_permission_denied_view