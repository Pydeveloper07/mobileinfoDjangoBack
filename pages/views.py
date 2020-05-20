from django.shortcuts import render
from listings.models import MobilePhone

def index(request):
    upcoming_phones = MobilePhone.objects.filter(status='upcoming')
    context = {
        'upcoming_phones': upcoming_phones,
    }
    return render(request, 'pages/index.html', context)
