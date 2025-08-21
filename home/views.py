from django.shortcuts import render, redirect
from .forms import ContactForm
from django.shortcuts import render
from .models import MenuItem
from django.shortcuts import render
from rest_framework import generics
from .models import AboutUs
from .serializers import AboutUsSerializer
from django.shortcuts import render, request
from .forms import ContactForm
from .models import OpeningHours
from .django.shortcuts import render
from .django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubscriberForm
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import render
from .models import RestaurantInfo
from django.shortcuts import render
from django.shortcuts import render
from .models import MenuItem
from django.shortcuts import render
from .models import RestaurantInfo
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render
from . models import MenuItem
from django.shortcuts import render, redirect, get_object_or_404
from . models import MenuItem
from django.shortcuts import render
from django.shortcuts import render
from . models import Restaurant
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from .models import Restaurant
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from .models import Restaurant
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import MenuItem
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
import os
from django.shortcuts import render
from django.conf import settings
from datetime import datetime
from django.shortcuts import render
from django.shortcuts import render
from .models import ContactInfo
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render






# Create your views here.
def contact_us_view(request):
    form = ContactForm(request.POST or None)
    if request.method =='POST' and form.is_valid():
        form.save()
        return redirect('home')
    
    return render(request, 'contact_us.html', {'form': form})

def contact_page(request):
    return render(request, 'contact.html')

def home(request):
    query = requests.GET.get('q')
    if query:
        menu_items = MenuItem.objects.filter(name___icontains=query)

    else:
        menu_items = MenuItem.objects.all()
    return render(request, 'home.html', {'menu_items': menu_items })

def home(request):
    restaurant = Restaurant.objects.all()
    return render(request, 'home.html', {'restaurant': restaurant})

class AboutUsSerializer(generics.RetrieveUpdateAPIView):
    queryset = AboutUs.generics.all()
    serializer_class = AboutUsSerializer
    
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def homepage_view(request):
    hours = OpeningHours.objects.all()
    return render(request, 'home.html', {'opening_hours': hours})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email =request.POST.get("email")
        message_text = request.POST.get("message")

        messages.success(request, "Thank you, your message has been sent!")
        return redirect('contact')
    return render(request, 'contact.html')


def homepage(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for subxcribing!")
            return redirect('home')
    else:
        form = SubscriberForm()
    return render(request, 'home.html', {'form': form})



def home(request):
    context = {
        'page_title': 'Spice Garden - Authentic Indian Cuisine in Hyderabad'
    }
    return render(request, 'home.html', context)

def reservations(request):
    return render(request, 'reservations.html')


def our_story(request):
    return render(request, 'our_story.html')



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        user_email = request.POST.get('email')
        message = request.POST.get('message')

    send_mail(
        subject="Thank you for contacting Spice Garden",
        message=(
            f"Hello {name},/n/n"
            "We have recieved your message and will get back to you shortly.\n\n 
            "Your Message:\n"
            f"{message}\n\n"
            "Warm regards, \nSpice Garden Team"
        ), 
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user_email],
        fail_silently=False,
    )
    return render(request, 'contact_sucess.html', {'name': name})

return render(request, 'contact.html')

def reservations(request):
    return render(request, 'reservations.html')

def privacy_policy(request):
    return render(request, 'privacy.html')

def gallery(request):
    return render(request, 'gallery.html')

def custom_permission_denied_view(request, exception=None):
    return render(request, 'errors/403.html', status=403)
    

def index(request):
    restaurant_info = RestaurantInfo.objects.first()
    return render(request, 'home/index.html', {"restaurant_info": restaurant_info})

def reservation_page(request):
    return render(request, 'home/reservation.html')


def menu_page(request):
    query = request.GET.get('q','')
    if query:
        items = MenuItem.objects.filter(name___icontains=query)
    else:
        items = MenuItem.objects.all()

    return render(request, 'home/menu.html', {
        'items': items,
        'query': query
    })

def home(request):
    info = RestaurantInfo.objects.first()
    return render(request, 'home/index.html', {'restaurant_info': info})



def careers(request):
    return render(request, 'careers.html')

def sitemap(request):
    return render(request, 'sitemap.html')

def thank_you(request):
    return render(request, 'thank_you.html')

def place_order(request):
    if request.method =='POST':
        return redirect('thank_you')

    return render(request, 'order_form.html')

def menu(request):
    items = MenuItem.objects.all()
    return render(request, 'menu.html', {'items': items})

def add_to_cart(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    cart = request.session.get('cart', {})

if str(item_id) in cart:
    cart[str(item_id)]['quantity'] += 1

else:
    cart[str(item_id)] = {
        'name': item.name,
        'price': float(item.price),
        'quantity': 1
    }

    request.session['cart'] = cart
    request.session.modified = True
    return redirect('menu')


def menu(request):
    item = MenuItem.objects.all()
    
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())

    return render(request, 'menu.html', {
        'items': items,
        'cart_total': total
    })


def view_cart(request):
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())

    return render(request, 'cart.html', {
        'cart': cart,
        'total': total
    })

def home(request):
    restaurant = Restaurant.objects.first()
    return render(request, 'home.html', {'restaurant': restaurant})

def reservations(request):
    return render(request, 'reservations.html')

def cart_view(request):
    return render(request, "cart.html")

def home_view(request):
    context = {
        restaurant = Restaurant.objects.first()
        'welcome_message': "Welcome to Our Restaurant! Enjoy the best food and Service."
        "restaurant_address": restaurant.address if restaurant else "Address coming soon..."
    }
    return render(request, "home.html", context)

def about_view(request):
    return render(request,"home/about.html")


def gallery(request):
    return render(request, 'home/gallery.html')

def about(request):
    return render(request, 'home/about.html')


def home(request):
    restaurant = Restaurant.objects.first()
    return render(request, 'home/index.html', {'restaurant': restaurant})

def menu(request):
    items = MenuItem.objects.all().order_by('category', 'name')
    paginator = Paginator(items, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home/menu.html', {'page_obj': page_obj})


def cart(request):
    cart_items = [
        {'name': 'Margherita Pizza', 'quantity': 2, 'price': 299},
        {"name": "Pasta Alfredo", "quantity": 1, "price": 350},
        {"name": "Chocolate cake", "quantity": 3, "price": 150}
    ]

    total = sum(item["price"]* item["quantity"] for item in cart_items)

    return render(request, "home/cart.html", {"cart_items": cart_items, "total": total})

def cart(request):
    return render(request, 'cart.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def privacy_policy(request):
    file_path = os.path.join(settings.BASE_DIR, 'templates', 'privacy.html')
    last_modified = os.path.getmtime(file_path)
    last_updated = datetime.fromtimestamp(last_modified).strftime("%B %d, %Y")
    return render(request, "privacy.html", {"last_updated": last_updated})

def privacy_policy(request):
    return render(request, "privacy.html")

def contact(request):
    contact_info = ContactInfo.objects.first()
    return render(request, "contact.html", {"contact_info": contact_info})

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def locations(request):
    return render(request, 'locations.html')

def terms_of_service(request):
    return render(request, "terms.html")