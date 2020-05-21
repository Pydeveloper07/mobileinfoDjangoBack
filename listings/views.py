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
