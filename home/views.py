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