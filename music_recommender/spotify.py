import requests
from django.conf import settings
import base64

SPOTIFY_API_BASE_URL = 'https://api.spotify.com/v1'

def search_tracks(query):
    url = f'{SPOTIFY_API_BASE_URL}/search'
    params = {'q': query, 'type': 'track'}
    headers = {'Authorization': f'Bearer {get_access_token()}'}
    response = requests.get(url, params=params, headers=headers)
    return response.json()

def get_access_token():
    url = 'https://accounts.spotify.com/api/token'
    headers = {'Authorization': f'Basic {get_auth_header()}'}
    data = {'grant_type': 'client_credentials'}
    response = requests.post(url, headers=headers, data=data)
    return response.json()['access_token']

def get_auth_header():
    client_id = settings.SPOTIFY_CLIENT_ID
    client_secret = settings.SPOTIFY_CLIENT_SECRET
    auth_header = f'{client_id}:{client_secret}'
    encoded_auth_header = base64.b64encode(auth_header.encode()).decode()
    return encoded_auth_header
