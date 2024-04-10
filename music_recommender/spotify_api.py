import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.conf import settings
from .models import Music

client_credentials_manager = SpotifyClientCredentials(client_id=settings.SPOTIFY_CLIENT_ID,
                                                      client_secret=settings.SPOTIFY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def search_song_with_features(query):
    results = sp.search(q=query, type='track', limit=1)
    if results['tracks']['items']:
        song_info = results['tracks']['items'][0]

        # Save the music data into the database
        Music.objects.create(
            title=song_info['name'],
            artist=song_info['artists'][0]['name'],
            genre=song_info['album']['genre']
        )

        features = {
            'name': song_info['name'],
            'artists': [artist['name'] for artist in song_info['artists']],
            'album': song_info['album']['name'],
            'release_date': song_info['album']['release_date'],
            'preview_url': song_info['preview_url'],
            'image_url': song_info['album']['images'][0]['url'],
            'tempo': song_info['tempo'],
            'energy': song_info['energy'],
            'popularity': song_info['popularity']
        }

        return features
    else:
        return None
