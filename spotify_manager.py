import os

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from song_model import Song

SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = 'http://localhost/'
SPOTIFY_MODIFY_SCOPE = 'playlist-modify-private'


class SpotifyManager:
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                                            client_secret=SPOTIFY_CLIENT_SECRET,
                                                            redirect_uri=SPOTIFY_REDIRECT_URI,
                                                            scope=SPOTIFY_MODIFY_SCOPE,
                                                            show_dialog=True,
                                                            cache_path="token.txt"))
        self.user = self.sp.current_user()['id']

    def create_playlist(self, name, songs: list[Song]):
        # 1 Create a new playlist (get the playlist id)
        playlist = self.sp.user_playlist_create(user=self.user,
                                                name=name,
                                                public=False,
                                                description=f'Billboard Top {len(songs)} for {name}')

        # 2 Find and populate the uris for the songs and add them to the playlist
        songs_uris = []
        for song in songs:
            try:
                track_data = self.sp.search(q=f'track: {song.name} year: {song.year} artist: {song.artist}',
                                            offset=0, type='track', limit=1)
            except IndexError:
                continue
            else:
                songs_uris.append(track_data['tracks']['items'][0]['uri'])

        # 3 Add the uris
        self.sp.playlist_add_items(playlist['id'], songs_uris)
