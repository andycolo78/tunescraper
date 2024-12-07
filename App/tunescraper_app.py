from App.page_scrapers.page_scraper import PageScraper
from App.services.requests_client import RequestsClient


class TunescraperApp:
    def __init__(self, url: str, page_scraper: PageScraper, requests_client: RequestsClient):
        self._page_scraper = page_scraper
        self._url = url
        self._requests_client = requests_client

    def get_releases(self) -> list:
        page_content = self._get_page_content(self._get_page_url(1))
        albums = self._get_albums_from_page(page_content)
        total_pages = self._get_total_pages(page_content)

        if total_pages == 1:
            return albums

        for num_page in range(2, total_pages+1):
            page_content = self._get_page_content(self._get_page_url(num_page))
            albums = [*albums, *self._get_albums_from_page(page_content)]
        return albums

    def _get_page_content(self, url: str) -> str:
        page_content = self._requests_client.get(url)
        return page_content

    def _get_albums_from_page(self, page) -> list:
        self._page_scraper.set_page(page)
        return self._page_scraper.albums

    def _get_total_pages(self, page: str) -> int:
        self._page_scraper.set_page(page)
        return self._page_scraper.num_pages

    def _get_page_url(self, num_page: int) -> str:
        if num_page == 1:
            return self._url

        return f"{self._url}{num_page}/"


