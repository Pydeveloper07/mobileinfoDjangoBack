from django.shortcuts import render, get_object_or_404, redirect
from .models import MobilePhone, Brand, Comment, PhoneReviews
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