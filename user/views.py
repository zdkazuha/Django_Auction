from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def user_login(request):
    if request.method == "POST":
        user = authenticate(
            request, 
            username=request.POST['username'], 
            password=request.POST['password'])
        if user is not None:
            login(request, user)
            messages.success(request, 'login success')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'logout success')
    return redirect('home')

def user_register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return render(request, "register.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, "register.html")

        User.objects.create_user(
            username=username,
            password=password1
        )

        user = authenticate(
            request,
            username=username,
            password=password1
        )
        login(request, user)
        messages.success(request, "Registration successful")
        return redirect("home")  

    return render(request, "register.html")