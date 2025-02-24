import time
import urllib.parse
import re

from App.data.release import Release
from App.helpers.progress_bar import ProgressBar
from App.services.metadata_client import MetadataClient
from App.exceptions.album_not_found_exception import AlbumNotFoundException
from App.exceptions.artist_not_found_exception import ArtistNotFoundException


class MetadataRepository:
    def __init__(self, metadata_client: MetadataClient):
        self._metadata_client = metadata_client

    def add_metadata(self, releases: list[Release]) -> list[Release]:

        print(f'Fetch metadata for {len(releases)} albums')
        for idx, release in enumerate(releases):
            ProgressBar.print(idx, len(releases))
            metadata = self._fetch_metadata(release)
            release.url = metadata[0]
            release.genres = metadata[1]
            releases[idx] = release
            time.sleep(1)
        return releases

    def _fetch_metadata(self, release: Release) -> tuple:
        try:
            unicode_title = re.sub(r'[^\x20-\x7E]', '', release.title)
            unicode_author = re.sub(r'[^\x20-\x7E]', '', release.author)

            release_metadata = self._metadata_client.search_album(unicode_title, unicode_author)
            artist_metadata = self._metadata_client.search_artist(unicode_author)

            return (
                release_metadata['external_urls']['spotify'] if release_metadata['external_urls'] else '',
                artist_metadata['genres'] if artist_metadata else []
            )

        except (AlbumNotFoundException, ArtistNotFoundException):
            return '', []


