from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import requests
from django.conf import settings
from users.models import UserProfile
from .models import MusicTrack
import base64

# Create your views here.

@login_required(login_url='users-login')
def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html', { 'title': 'About' })

