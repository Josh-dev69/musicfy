import os
import requests
import base64

SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

def get_spotify_access_token():
    url = 'https://accounts.spotify.com/api/token'
    headers = {'Authorization': 'Basic ' + base64.b64encode(f'{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}'.encode()).decode()}
    data = {'grant_type': 'client_credentials'}
    response = requests.post(url, headers=headers, data=data)
    response_data = response.json()
    access_token = response_data.get('access_token')
    return access_token

def search_music_tracks(query):
    access_token = get_spotify_access_token()
    url = 'https://api.spotify.com/v1/search'
    headers = {'Authorization': 'Bearer ' + access_token}
    params = {'q': query, 'type': 'track'}
    response = requests.get(url, headers=headers, params=params)
    response_data = response.json()
    return response_data.get('tracks', {}).get('items', [])
