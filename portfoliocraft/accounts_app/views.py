from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "This username is already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "This email is already registered")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                print(f"User {user.username} with email {user.email} has been successfully created.")
                return redirect('login')
        else:
            messages.info(request, "Passwords do not match")
            return redirect('register')
    return render(request, "accounts/register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            print(f"User {user} authenticated successfully")
            auth_login(request, user)  
            return redirect('homepage')
        else:
            print("Authentication failed")
            messages.info(request, "Please provide correct details")
            return redirect('login')
    return render(request, 'accounts/login.html')

def logout(request):
    auth_logout(request)  
    return redirect('login')

def Homepage(request):
    return render(request, 'portfolio/homepage.html')
