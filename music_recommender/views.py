from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='users-login')
def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html', { 'title': 'About' })