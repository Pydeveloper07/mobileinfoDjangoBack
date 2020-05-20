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

@login_required
def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are now logged out!")
        return redirect('index')
        

def register(request):
    if request.method == "POST":
        first_name = last_name = username = email = password = conf_password = ''
        if request.POST['first_name']:
            first_name = request.POST['first_name']
        if request.POST['last_name']:
            last_name = request.POST['last_name']
        if request.POST['username']:
            username = request.POST['username']
        else:
            messages.error(request, "Username required!")
            return redirect('index')
        if request.POST['email']:
            email = request.POST['email']
        if request.POST['password']:
            password = request.POST['password']
        if request.POST['conf_password']:
            conf_password = request.POST['conf_password']
        if User.objects.filter(username=username).exists():
            messages.error(request, "This username already exists! Try another!")
            return redirect('index')
        if User.objects.filter(email=email).exists():
            messages.error(request, "This email already in use!")
            return redirect('index')
        else:
            if password == conf_password and len(password) >= 6:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                user.save()
                messages.success(request, "You have successfully registered!")
                return redirect('index')
            else:
                messages.error(request, "Password length shouldn't be less than 6 characters!")
                return redirect('index')

        

