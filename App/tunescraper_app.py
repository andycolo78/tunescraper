from App.repositories.metadata_repository import MetadataRepository
from App.repositories.releases_repository import ReleasesRepository
from App.data.release import Release


class TunescraperApp:
    def __init__(self, releases_repository: ReleasesRepository, metadata_repository: MetadataRepository):
        self._releases_repository = releases_repository
        self._metadata_repository = metadata_repository

    def get_releases(self) -> list[Release]:
        scraped_releases = self._releases_repository.fetch_releases()
        complete_releases = self._metadata_repository.add_metadata(scraped_releases)
        return complete_releases



