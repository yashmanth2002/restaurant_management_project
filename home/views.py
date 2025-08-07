from django.shortcuts import render, redirect
from .forms import ContactForm
from django.shortcuts import render
from .models import MenuItem
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