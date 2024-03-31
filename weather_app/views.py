from django.shortcuts import render
from .weather_api import get_weather_data
from django.http import HttpResponse
from django.core.mail import send_mail
def weather_view(request):
    if request.method == 'POST':
        city_name = request.POST.get("city_name")
        weather_data = get_weather_data(city_name)
        return render(request, 'weather.html', {'weather_data': weather_data})
    else:
        return render(request, 'weather.html')





def send_email_view(request):
    subject = 'Hello from Django!'
    message = 'This is a test email sent from Django.'
    from_email = 'k4cp3rr0@808dev.me'
    recipient_list = ['root@808dev.me', 'kacper.cichorski@gmail.com']
    send_mail(subject, message, from_email, recipient_list)
    return HttpResponse('Email sent successfully!')
