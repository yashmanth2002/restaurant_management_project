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
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from . import views
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.urls import path
from . import views
from django.urls import path
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
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
from django.urls import path
from . import views
from django.urls import path
from . import views
from django.urls import path
from . import views
from django.urls import path
from . import  views
from django.urls import path
from . import views
from django.urls import path
from . import views
from django.urls import path
from django.views.generic import TemplateView
from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.urls import path
from .views import faq_view
from django.urls import path
from . import views
handler403 = "home.views.custom_403"
handler403 = "home.views.custom_403"


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
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    pth("privacy-policy/", views.privacy_policy, name="privacy_policy")
    path("submit-review/", views.submit_reviews, name="submit_review"),
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path('', views.home, name='home'),
    path('privacy/', vies.privacy_policy, name="privacy")
    path('clear-cart/', views.clear_cart, name='clear_cart'),
    path("logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),
    path("privacy-policy/", views.privacy_policy_view, name="privacy_policy"),
    path('reviews/', views.reviews_list, name='reviews_list'),
    path('menu/', views.menu_list, name='menu_list'),
    path('blog/', views.blog_placeholder, name='blog_placeholder')
    path('privacy/', views.privacy_policy, name='privacy_policy'),
    path('reservations/', views.reservations, name='reservations'),
    path('reservations/', views.reservations, name='reservations')
    path('gallery', views.gallery, name='gallery'),
    path('faq/', views.faq, name='faq'),
    path('menu/', viewa.menu, name='menu'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    path('privacy', views.privacy_policy, name="privacy_policy")
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy")
    path("faq/", views.faq, name="faq")
    path("contact/", views.contact, name="contact"),
    path("thank-you/", views.thank_you, name="thank_you"),
    path('', views.home_view, name='home'),
    path('menu/', views.menu_view, name='menu')
    path("contact/", views.contact_us, name="contact_us"),
    path("", views.home, name="home"),
    path("menu/", views.menum name="menu"),
    path("contact/", views.contact_us, name="contact_us"),
    path("specials/", views.specials, name="specials")
    path("thank-you/", TemplateView.as_view(template_name="thank_you.html"), name="thank_you")
    path("contact/", views.contact_view, name="contact"),
    path("thank-you-contact/", TemplateView.as_view(
        template_name = "thank_you_contact.html"
      ),  name="thank_you_contact"),

      path("about/", views.about_view, name="about"),

      path("order/", views.place_order, name="place_order"),
      path("order/thank-you/", TemplateView.as_view(
        template_name = "order_thank_you.html"
      ), name="order_thank_you"),
      path("faq/", faq_view, name="faq"),
      path("", home, name="home"),
      path('menu/', views.menu, name='menu'),
      path('contact/', views.contact, name="contact"),
      path('reservations/', views.reservation, name="Reservations"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = view.custom_permission_denied_view
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)