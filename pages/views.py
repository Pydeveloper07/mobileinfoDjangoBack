from django.shortcuts import render, redirect
from listings.models import MobilePhone
from django.core.mail import BadHeaderError, send_mail
from django.contrib import messages

def index(request):
    upcoming_phones = MobilePhone.objects.filter(status='upcoming')
    context = {
        'upcoming_phones': upcoming_phones,
    }
    return render(request, 'pages/index.html', context)

def send_email(request):
    if request.method == "POST":
        name = subject = email = message = ''
        if request.POST['name']:
            name = request.POST['name']
        if request.POST['email']:
            email = request.POST['email']
        if request.POST['subject']:
            subject = request.POST['subject']
        if request.POST['message']:
            message = request.POST['message']
        if email and message:
            try:
                send_mail(
                    "From: " + email + "\n" + subject, 
                    message, 
                    'blacktigerno1ever@gmail.com', 
                    ['inha07111999@gmail.com'],
                    fail_silently=False
                    )
                messages.success(request, "Thank you for contacting with us!")
                return redirect('index')
            except BadHeaderError:
                messages.error(request, "Invalid header found!")
                return redirect('index')
            except:
                messages.error(request, "Something went wrong try again")
                return redirect('index')
        else:
            messages.error(request, "Make sure you provided email and you message!")
            return redirect('index')

