from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from api_integration.spotify_data import fetch_music_data, enhance_recommendations
from music_recommender.models import MusicTrack

# Create your views here.

def about(request):
    return render(request, 'main/about.html', { 'title': 'About' })

@login_required(login_url='users-login')
def generate_recommendations(request):
    """
    View to display personalized music recommendations to the user.
    """
    # Fetch user preferences (you may need to modify this based on your implementation)
    user_preferences = {
        'favorite_artist': request.user.userprofile.favorite_artist,
        'keywords': [],  # Add logic to extract keywords from user preferences
    }

    # Fetch music data from Spotify
    fetched_tracks = fetch_music_data(
        artist=user_preferences['favorite_artist'],
        limit=50
    )

    
    # Enhance recommendations using keyword matching
    recommended_tracks = enhance_recommendations(user_preferences, fetched_tracks)

    return render(request, 'main/home.html', {'recommended_tracks': recommended_tracks})