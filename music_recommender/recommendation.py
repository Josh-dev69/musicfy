import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from .spotify_api import search_song_with_features
from .models import UserProfile

def generate_personalized_recommendations(user):
    # Retrieve user preferences
    user_profile = UserProfile.objects.get(user=user)
    favorite_genres = user_profile.favorite_genres.all()
    favorite_artists = user_profile.favorite_artists.all()
    favorite_songs = user_profile.favorite_songs.all()

    # Aggregate user preferences
    user_preferences = set()
    for genre in favorite_genres:
        user_preferences.add(genre)
    for artist in favorite_artists:
        user_preferences.add(artist)
    for song in favorite_songs:
        user_preferences.add(song)

    # Generate recommendations based on user preferences
    recommendations = []
    for preference in user_preferences:
        song_info = search_song_with_features(preference)
        if song_info:
            recommendations.append(song_info)

    return recommendations