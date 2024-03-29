from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegisterForm, UserLoginForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} has been created!')
        return redirect('users-login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'title': 'About'})

# Login View
def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request,("You have been Logged in"))
                return redirect('musicify-home')  # Redirect to home page after login
            else:
                messages.error(request, 'Invalid username or password.')
                return redirect('users-login')  # Redirect to home page after login
    else:
        return render(request, 'users/login.html', {'form': form, 'title': 'Login'})

# Logout View
def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out..."))
    return redirect('musicify-home')