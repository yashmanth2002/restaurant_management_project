from django.shortcuts import render
from .models import Restaurant
from django.db import models
from django.shortcuts import render
from .models import RestaurantInfo
from django.shortcuts import render
from .models import RestaurantInfo
import smtplib
from email.mime.text import MIMEText,
from django.shortcuts import render, redirect
from django.conf import settings


def contact_view(request):
    if request.mehod == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        subject = f"New Contact From Submission from {name}"
        body = f"""
        You have a new Message from your website contact form:
        

        Name: {name}
        Email: {email}
        Message: {message}
        """
        try:
            smtp_server = "smtp.google.com"
            smtp_port = 587
            sender_email = settings.DEFAULT_FROM_EMAIL
            sender_password = settings.EMAIL_HOST_PASSWORD
            recipient_email = settings.CONTACT_RECIEVER_MAIL

            msg = MIMEText(body)
            msg["SUBJECT"] = subject
            msg["FROM"] = sender_email
            msg["TO"] = recipient_email

            with smptlib.SMTP(smtp_server, smtp_port)as server:
                server.startls()
                server.login(sender_email, sender_password)
                server.sendemail(sender_email, recipient_email, msg.as_string())

            print("Email sent sucessfully!")

        except Exception as:
            print("Error sending email:", e)

        return redirect("thank_you_contact")

    return render(request, "contact.html")

# Create your views here.

def homepage(request):
    restaurant = Restaurant.objects.first()

    context = {
        'restaurant_name': restaurant.name if restaurant else 'Your Restaurant'
    }
    return render(request, 'home.html', context)

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

def about_us_view(request):
    info = RestaurantInfo.objects.first()
    return render(request, 'about_us.html', {'info': info})

def contact_us(request):
    restaurant_info = RestaurantInfo.objects.first()
    return render(request, 'home/contact.html', {'restaurant_info': restaurant_info})