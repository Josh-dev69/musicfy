from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            if User.objects.filter(email=email).exists():
                messages.info(request, f'Email Already exists')
                return redirect('users-register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, f'Username Already exists')
                return redirect('users-register')
            else:        
                myuser = User.objects.create_user(username, email, pass1)
                myuser.first_name = fname
                myuser.last_name = lname
                
                myuser.save()

                user_login = authenticate(request, username=username, password=pass1)
                login(request, user_login)
                return redirect('musicify-home')
        else:
            messages.info(request, f'Mismatched Password')
            return redirect('users-register')

    return render(request, 'users/register.html')

# Login View
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(request, username=username, password=pass1)

        if user is not None:
            login(request, user)
            return redirect('musicify-home')  # Redirect to home page after login
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('users-login')  # Redirect to home page after login
    else:
        return render(request, 'users/login.html')

# Logout View
@login_required(login_url='users-login')
def logout_user(request):
    logout(request)
    messages.info(request, 'You have Logged out')
    return redirect('musicify-home')


@login_required(login_url='users-login')
def user_preference(request):
    return render(request, 'users/preferences.html')