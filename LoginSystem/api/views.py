from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.cache import never_cache

# Index View
def index(request):
    return render(request, 'api/index.html')

# Register View
def user_register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        User = get_user_model()
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        messages.success(request, "Registration complete, you can login now")
        return redirect('login')
    return render(request, 'api/register.html')

# Login View
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect('home')

        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'api/login.html')

# Home View (Protected)
@login_required(login_url='login')
@never_cache
def home(request):
    return render(request, 'api/home.html')

# Logout View
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('index')
