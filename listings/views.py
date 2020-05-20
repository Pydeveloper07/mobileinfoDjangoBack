from django.shortcuts import render, get_object_or_404
from .models import MobilePhone, Brand, Comment
from django.http import HttpResponse
import json
from django.contrib.auth.decorators import login_required

def listings(request):
    brands = Brand.objects.all()
    wk_phone = MobilePhone.objects.get(is_wkp=True)
    context = {
        'brands': brands,
        'wk_phone': wk_phone,
    }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    phone = get_object_or_404(MobilePhone, pk=listing_id)
    context = {
        'phone':phone,
    }
    return render(request, 'listings/listing.html', context)

@login_required
def like(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        phone = get_object_or_404(MobilePhone, id=id)
        if phone:
           phone.likes += 1
           phone.save()
    
        context = {
            'likes': phone.likes,
            'id': phone.id,
        }
        return HttpResponse(json.dumps(context), content_type='applications/json')