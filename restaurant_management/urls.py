"""
URL configuration for restaurant_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.urls import path
from .views import feedback_view
from .import views
from django.conf import settings
from django.conf.urls.static import static
from .views import contact_view, success_view
from .views import contact_view
from django.urls import include,path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('home.urls')),
    path('api/accounts/',include('account.urls')),
    path('api/products/',include('products.urls')),
    path('api/orders/',include('orders.urls')),
    path('feedback/', feedback_view, name='feedback'),
    path('', views.homepage, name='homepage'),
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('contact/', contact_view, name='contact')
    path('success/', success_view, name='success')
    path('contact/', contact_view, name='contact'),
    path('', include('contact.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)