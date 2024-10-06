import undetected_chromedriver as uc

from App.page_scrapers.page_scraper import PageScraper
from App.services.requests_client import RequestsClient


class Tunescraper:
    def __init__(self, url: str, page_scraper: PageScraper, requests_client: RequestsClient):
        self._page_scraper = page_scraper
        self._url = url
        self._requests_client = requests_client

    def get_releases(self) -> list:
        albums = []
        for num_page in range(1, self._get_total_pages()+1):
            page_content = self._get_page_content(self._get_page_url(num_page))
            albums = [*albums, *self._get_albums_from_page(page_content)]
        return albums

    def _get_page_content(self, url: str) -> str:
        page_content = self._requests_client.get(url)
        return page_content

    def _get_albums_from_page(self, page) -> list:
        self._page_scraper.set_page(page)
        return self._page_scraper.albums

    def _get_total_pages(self) -> int:
        return 1

    def _get_page_url(self, num_page: int) -> str:
        if num_page == 1:
            return self._url

        return f"{self._url}{num_page}/"



