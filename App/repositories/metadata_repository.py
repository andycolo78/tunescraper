import urllib.parse

from App.data.release import Release
from App.services.metadata_client import MetadataClient


class MetadataRepository:
    def __init__(self, metadata_client: MetadataClient):
        self._metadata_client = metadata_client

    def add_metadata(self, releases: list[Release]) -> list[Release]:
        for idx, release in enumerate(releases):
            metadata = self._fetch_metadata(release)
            release.url = metadata[0]
            release.genres = metadata[1]
            releases[idx] = release
        return releases

    def _fetch_metadata(self, release: Release) -> tuple:
        # title = urllib.parse.quote(release.title)
        # author = urllib.parse.quote(release.author)
        #
        # release_metadata = self._metadata_client.search(
        #     q=f'{title}artist:{author}', limit=1, type='album')
        # artist_metadata = self._metadata_client.search(q=author, limit=1, type='artist')

        release_metadata = self._metadata_client.search_album(release.title, release.author)
        artist_metadata = self._metadata_client.search_artist(release.author)

        return (
            release_metadata['external_urls']['spotify'] if release_metadata['external_urls'] else '',
            artist_metadata['genres'] if artist_metadata else []
        )


