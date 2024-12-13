from App.page_scrapers.page_scraper import PageScraper
from App.parsers.release_parser import ReleaseParser


class MockPagesScraper:
    def __init__(self, release_parser: ReleaseParser, releases=None, num_pages=0):
        self._releases = releases
        self._page = None
        self._num_pages = num_pages

    def set_page(self, page):
        self._page = page

    @property
    def releases(self):
        return self._releases

    @property
    def num_pages(self):
        return self._num_pages


