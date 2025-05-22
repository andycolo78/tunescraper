from App.repositories.releases_repository import ReleasesRepository
from App.data.release import Release


class TunescraperApp:
    def __init__(self, releases_repository: ReleasesRepository):
        self._releases_repository = releases_repository

    def get_releases(self) -> list[Release]:
        return self._releases_repository.fetch_releases()


