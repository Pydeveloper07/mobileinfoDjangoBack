from django.shortcuts import render, get_object_or_404, redirect
from .models import MobilePhone, Brand, Comment, PhoneReviews, CommentLikes, PhoneLikes
from django.contrib.auth.models import User
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
    if request.user.is_authenticated:
        new_review, old_review = PhoneReviews.objects.get_or_create(username=request.user, phone_id=MobilePhone.objects.get(id=listing_id))
    context = {
        'phone':phone,
    }
    return render(request, 'listings/listing.html', context)

@login_required
def add_comment(request):
    if request.method == "POST":
        phone_id = request.POST['phone_id']
        username = request.POST['name']
        content = request.POST['content']
        comment = Comment.objects.create(content=content)
        comment.user_name = User.objects.get(username=username)
        comment.phone_id = MobilePhone.objects.get(id=phone_id)
        if request.POST['reply_id']:
            reply_id = request.POST['reply_id']
            comment.reply_id = Comment.objects.get(id=reply_id)
        comment.save()
        return redirect('listing', phone_id)

def like(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            context = {
                'login_needed': True,
            }
            return HttpResponse(json.dumps(context), content_type='applications/json')
        id = request.POST['id']
        phone = get_object_or_404(MobilePhone, id=id)
        new, created = PhoneLikes.objects.get_or_create(username=request.user, phone_id=phone)
        context = {
            'login_needed': False,
            'like': True,
        }
        if not created:
            PhoneLikes.objects.get(username=request.user, phone_id=phone).delete()
            context['like'] = False
        context['numOfLikes'] = phone.likes.count()
        return HttpResponse(json.dumps(context), content_type='applications/json')

def like_comment(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            context = {
                'login_needed': True,
            }
            return HttpResponse(json.dumps(context), content_type='applications/json')
        id = request.POST['comment_id']
        comment = get_object_or_404(Comment,id=id)
        new, created = CommentLikes.objects.get_or_create(username=request.user, comment_id=comment)
        context = {
            'login_needed': False,
            'like': True,
            }
        if not created:
            CommentLikes.objects.get(username=request.user, comment_id=comment).delete()
            context['like'] = False
        context['numOfLikes'] = comment.likes.count()
        return HttpResponse(json.dumps(context), content_type='applications/json')

def search(request):
    phones = MobilePhone.objects.all()
    brand = city = state = ''
    weight = ram = storage = price = 0

    # Filtering by brand
    if 'brand' in request.POST:
        if request.POST['brand']:
            brand = str(request.POST['brand']).lower().capitalize()
            phones = phones.filter(brand__exact=brand)
    
    # Filtering by price
    if 'price' in request.POST:
        if request.POST['price']:
            price = int(request.POST['price'])
            if price == 900:
                phones = phones.filter(price__gte=price)
            else:
                phones = phones.filter(price__lte=price)

    # Filtering by weight            
    if 'weight' in request.POST:
        if request.POST['weight']:
            phones = phones.filter(weight__lte=request.POST['weight'])

    # Filtering by RAM
    if 'ram' in request.POST:
        if request.POST['ram']:
            ram = int(request.POST['ram'])
            if ram == 10:
                for phone in phones:
                    if ',' in phone.ram:
                        rams = str(phone.ram).split(',')
                        is_exist = False
                        for r in rams:
                            if int(r) >= ram:
                                is_exist = True
                        if not is_exist:
                            phones = phones.exclude(ram=phone.ram)
                    else:
                        if int(phone.ram) < ram:
                            phones = phones.exclude(ram=phone.ram)
            else:
                for phone in phones:
                    if ',' in phone.ram:
                        rams = str(phone.ram).split(',')
                        is_exist = False
                        for r in rams:
                            if int(r) == ram:
                                is_exist = True
                        if not is_exist:
                            phones = phones.exclude(ram=phone.ram)
                    else:
                        if int(phone.ram) != ram:
                            phones = phones.exclude(ram=phone.ram)

    # Filtering by Storage
    if 'storage' in request.POST:
        if request.POST['storage']:
            storage = int(request.POST['storage'])
            if storage == 512:
                for phone in phones:
                        if ',' in phone.storage:
                            storages = str(phone.storage).split(',')
                            is_exist = False
                            for s in storages:
                                if int(s) >= storage:
                                    is_exist = True
                            if not is_exist:
                                phones = phones.exclude(storage=phone.storage)
                        else:
                            if int(phone.storage) < storage:
                                phones = phones.exclude(storage=phone.storage)
            else:
                for phone in phones:
                    if ',' in phone.storage:
                        storages = str(phone.storage).split(',')
                        is_exist = False
                        for s in storages:
                            if int(s) == storage:
                                is_exist = True
                        if not is_exist:
                            phones = phones.exclude(storage=phone.storage)
                    else:
                        if int(phone.storage) != storage:
                            phones = phones.exclude(storage=phone.storage)
    
    # Filtering by CPU
    if 'cpu' in request.POST:
        if request.POST['cpu']:
            phones = phones.filter(cpu_type__iexact=request.POST['cpu'])

    # Filtering by Selfie Camera
    if 'selfie_camera' in request.POST:
        if request.POST['selfie_camera']:
            selfie_camera = request.POST['selfie_camera']
            if selfie_camera == 'triple':
                phones = phones.filter(sc_type='triple').filter(sc_type='triple+')
            else:
                phones = phones.filter(sc_type__iexact=selfie_camera)
    
    # Filtering by Main Camera
    if 'main_camera' in request.POST:
        if request.POST['main_camera']:
            main_camera = request.POST['main_camera']
            if main_camera == 'triple':
                phones = phones.filter(mc_type='triple').filter(mc_type='triple+')
            else:
                phones = phones.filter(mc_type__exact=main_camera)

    # Filtering by Battery Capacity
    if 'battery' in request.POST:
        if request.POST['battery']:
            battery = int(request.POST['battery'])
            if battery == 1000:
                phones = phones.exclude(battery_capacity__gt=battery+1000)
            elif battery == 2000:
                phones = phones.exclude(battery_capacity__lte=battery).exclude(battery_capacity__gt=battery+1000)
            elif battery == 3000:
                phones = phones.exclude(battery_capacity__lte=battery).exclude(battery_capacity__gt=battery+1000) 
            elif battery == 4000:
                phones = phones.filter(battery_capacity__gt=battery)
    
    context = {
        'phones': phones,
    }
    return render(request, 'pages/search.html', context)