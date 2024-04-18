import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def authenticate_spotify():
    """
    Authenticate with the Spotify API using client credentials flow.
    Returns a Spotipy client object.
    """
    # Get your Spotify API credentials from environment variables
    client_id = os.environ.get('SPOTIFY_CLIENT_ID')
    client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')

    # Authenticate with the Spotify API
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    
    return sp
