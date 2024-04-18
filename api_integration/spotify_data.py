from .spotify_api import authenticate_spotify
from music_recommender.models import MusicTrack

def fetch_music_data(genre=None, artist=None, limit=10):
    """
    Fetch music data from Spotify based on user preferences.
    Returns a list of music tracks with relevant metadata.
    """
    sp = authenticate_spotify()

    # Construct the query based on user preferences
    query = ''
    if genre:
        query += f'genre:"{genre}"'
    if artist:
        query += f' artist:"{artist}"'

    try:
        # Search for tracks on Spotify
        results = sp.search(q=query, type='track', limit=limit)
    except Exception as e:
        print(f"An error occurred while fetching music data: {e}")
        return []

    # Extract relevant metadata for each track and save to the database
    tracks = []
    for track in results['tracks']['items']:
        title = track['name']
        artist = track['artists'][0]['name']
        # Check if the track already exists in the database
        music_track, created = MusicTrack.objects.get_or_create(
            title=title,
            artist=artist,
        )
        # Add the music track to the list
        tracks.append(music_track)

    return tracks


def enhance_recommendations(user_preferences, fetched_tracks):
    """
    Enhance content-based recommendations using keyword matching.
    Returns a list of filtered music tracks based on user preferences.
    """
    preferred_artist = user_preferences.get('favorite_artist')
    keywords = user_preferences.get('keywords')

    # Filter fetched tracks based on user preferences and keyword matching
    filtered_tracks = []
    for track in fetched_tracks:
        if preferred_artist and track.artist == preferred_artist:
            filtered_tracks.append(track)
        elif keywords:
            for keyword in keywords:
                if keyword.lower() in track.title.lower():
                    filtered_tracks.append(track)
                    break

    return filtered_tracks
