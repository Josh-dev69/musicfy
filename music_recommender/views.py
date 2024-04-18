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
    Generate personalized music recommendations for the user.
    """
    # Get user preferences from the request (you may have a different method to obtain user preferences)
    user_preferences = {
        'favorite_artist': request.user.userprofile.favorite_artist,
        'keywords': [],  # You may need to extract keywords from other user preferences
    }

    # Fetch music data from Spotify based on user preferences
    fetched_tracks = fetch_music_data(
        artist=user_preferences.get('favorite_artist'),
        limit=50  # Adjust the limit as needed
    )

    # Enhance recommendations using keyword matching
    filtered_tracks = enhance_recommendations(user_preferences, fetched_tracks)

    # Pass the filtered tracks to the template for display
    context = {
        'tracks': filtered_tracks,
    }
    return render(request, 'main/home.html', context)