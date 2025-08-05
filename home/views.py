from django.shortcuts import render, redirect
from .forms import ContactForm
# Create your views here.
def contact_us_view(request):
    form = ContactForm(request.POST or None)
    if request.method =='POST' and form.is_valid():
        form.save()
        return redirect('home')
    
    return render(request, 'contact_us.html', {'form': form})
