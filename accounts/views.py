from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth, messages


def login(request):
    if request.method == "POST":
        if request.POST['username']:
            username = request.POST['username']
        else:
            username = ''
        if request.POST['password']:
            password = request.POST['password']
        else:
            password = ''
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in!")
            return redirect('index')
        else:
            messages.error(request, "Wrong credentials!")
            return redirect('index')
    else:
        return render(request, 'pages/index.html')

def logout(request):
    pass

def register(request):
    pass
