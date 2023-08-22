# spotify_app/spotify_auth.py
from spotipy.oauth2 import SpotifyOAuth
from django.conf import settings

def get_spotify_auth():
    return SpotifyOAuth(
        settings.SPOTIFY_CLIENT_ID,
        settings.SPOTIFY_CLIENT_SECRET,
        settings.SPOTIFY_REDIRECT_URI,
        scope='user-library-read user-modify-playback-state',
    )
