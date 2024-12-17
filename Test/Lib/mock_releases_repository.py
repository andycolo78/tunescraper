from App.data.release import Release
from App.page_scrapers.page_scraper import PageScraper
from App.repositories.releases_repository import ReleasesRepository
from App.services.requests_client import RequestsClient


class MockReleasesRepository(ReleasesRepository):

    def __init__(self, url: str, page_scraper: PageScraper, requests_client: RequestsClient, mocked: list[Release]):
        super().__init__(url, page_scraper, requests_client)
        self._mocked = mocked

    def fetch_releases(self) -> list[Release]:
        return self._mocked



