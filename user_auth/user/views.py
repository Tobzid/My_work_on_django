from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already in Used.')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already in used')
                return redirect('register')
            else:
                User = User.objects.create_user(username=username, email=email, password=password)
                User.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not the same.')
            return redirect('register')
    else:
        return render(request, 'register.html')
