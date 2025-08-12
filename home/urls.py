from django.urls import path
from .views import menu_view
from .views import home
from . import views
from django.conf.urls.static import static 
from .views import submit_feedback
from django.urls import path
from .views import contact_view, thank_you_view

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

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)