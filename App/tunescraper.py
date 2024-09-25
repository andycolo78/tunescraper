import requests

from App.page_scrapers.page_scraper import PageScraper


class Tunescraper:
    def __init__(self, page_scraper: PageScraper):
        self.page_scraper = page_scraper

    def get_releases(self):
        pass

    def _get_page_content(self, url: str) -> str:
        page_content = requests.get(url).content
        print(page_content)
        return str(page_content)

    def _get_albums_from_page(self, page) -> list:
        self.page_scraper.set_page(page)
        return self.page_scraper.albums

