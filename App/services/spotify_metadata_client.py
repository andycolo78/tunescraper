import urllib.parse
import re

from App.services.metadata_client import MetadataClient
from spotipy import Spotify


class SpotifyMetadataClient(MetadataClient):

    def __init__(self, spotify: Spotify):
        self._spotify = spotify

    def search_album(self, title: str, artist: str) -> dict:
        quote_title = urllib.parse.quote(re.sub(r'\W+', '', title))
        quote_artist = urllib.parse.quote(re.sub(r'\W+', '', artist))
        result = self._spotify.search(q=f'{quote_title}%20artist:{quote_artist}', limit=1, type='album')

        return result['albums']['items'][0] if result['albums']['items'] else {}

    def search_artist(self, artist: str) -> dict:
        quote_artist = urllib.parse.quote(re.sub(r'\W+', '', artist))
        result = self._spotify.search(q=quote_artist, limit=1, type='artist')

        return result['artists']['items'][0] if result['artists']['items'] else {}
