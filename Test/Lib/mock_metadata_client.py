from App.services.metadata_client import MetadataClient


class MockMetadataClient(MetadataClient):

    def __init__(self, album_response: list = None, artist_response: list = None):
        self._album_response = album_response
        self._artist_response = artist_response

    def search_album(self, title: str, artist: str) -> dict:
        for album_meta in self._album_response:
            if album_meta['name'] == title:
                return album_meta

    def search_artist(self, artist: str) -> dict:
        for artis_meta in self._artist_response:
            if artis_meta['name'] == artist:
                return artis_meta
