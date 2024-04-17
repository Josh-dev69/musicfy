from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from users.models import UserProfile
from .spotify import search_music_tracks

# Create your views here.

@login_required(login_url='users-login')
def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html', { 'title': 'About' })



def recommendation_list(request):
    # Search for music tracks
    query = 'your_search_query'
    music_tracks = search_music_tracks(query)
    
    context = {
        'music_tracks': music_tracks
    }
    return render(request, 'recommendations/recommendation_list.html', context)
