import urllib.parse
import re

import unicodedata

from App.init.logger_factory import LoggerFactory

from App.services.metadata_client import MetadataClient
from App.exceptions.album_not_found_exception import AlbumNotFoundException
from App.exceptions.artist_not_found_exception import ArtistNotFoundException
from spotipy import Spotify
from difflib import SequenceMatcher


class SpotifyMetadataClient(MetadataClient):

    ALBUM_MATCH_RATIO = 0.8
    ARTIST_MATCH_RATIO = 0.4

    def __init__(self, spotify: Spotify):
        self._spotify = spotify
        self._logger = LoggerFactory.get_logger(__name__)

    def search_album(self, title: str, artist: str) -> dict:
        clean_title = self._clean_string(title)
        clean_artist = self._clean_string(artist)

        search_string = f'{clean_title} artist:{clean_artist}'

        self._logger.debug(f'Title : {clean_title} | Artist : {clean_artist} | q : {search_string}')

        result = self._spotify.     search(q=search_string, limit=5, type="album")
        self._logger.debug(f'album search result : {result}')

        return self._get_album_metadata(title, artist, result)

    def search_artist(self, artist: str) -> dict:
        clean_artist_list = re.split(r'[&,]', self._clean_string(artist))
        clean_artist = clean_artist_list[0]

        self._logger.debug(f'Artist : {clean_artist} | q : {clean_artist}')

        result = self._spotify.search(q=clean_artist, limit=10, type="artist")

        self._logger.debug(f'artist search result : {result}')
        return self._get_artist_metadata(artist, result)

    def _clean_string(self, input_string: str) -> str:
        normalized_string = unicodedata.normalize('NFD', input_string)
        unaccented_string = ''.join(char for char in normalized_string if not unicodedata.combining(char))
        cleaned_string = re.sub(r'[^a-zA-Z0-9 &$£()-]', '', unaccented_string)
        return cleaned_string

    def _get_album_metadata(self, title: str, artist: str, response: dict) -> dict:
        if not response['albums']['items']:
            raise AlbumNotFoundException(f'Album {title} by {artist} : Spotify response empty')

        for album_metadata in response['albums']['items']:
            album_match_score = SequenceMatcher(None, album_metadata['name'].lower(), title.lower()).ratio()

            self._logger.debug(f'Album title : {title} VS {album_metadata['name']} | Match score : {album_match_score}')

            if album_match_score < self.ALBUM_MATCH_RATIO:
                continue

            for artist_metadata in album_metadata['artists']:
                artist_match_score = SequenceMatcher(None, artist_metadata['name'].lower(), artist.lower()).ratio()

                self._logger.debug(f'Album artist : {artist} VS {artist_metadata['name']}| Match score : {artist_match_score}')

                if artist_match_score > self.ARTIST_MATCH_RATIO:
                    return album_metadata

        raise AlbumNotFoundException(f'Album {title} by {artist} : not found in Spotify response',
                                     response['albums']['items'])

    def _get_artist_metadata(self, artist: str, response: dict) -> dict:
        if not response['artists']['items']:
            raise ArtistNotFoundException(f'Artist {artist} : Spotify response empty')

        for artist_metadata in response['artists']['items']:
            artist_match_score = SequenceMatcher(None, artist_metadata['name'].lower(), artist.lower()).ratio()

            self._logger.debug(f'Artist : {artist} VS {artist_metadata['name']}| Match score : {artist_match_score}')

            if artist_match_score > self.ARTIST_MATCH_RATIO:
                return artist_metadata

        raise ArtistNotFoundException(f'Artist {artist} : not found in Spotify response', response['artists']['items'])
