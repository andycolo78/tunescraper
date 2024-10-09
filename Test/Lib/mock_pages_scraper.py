from App.page_scrapers.page_scraper import PageScraper
from App.parsers.album_parser import AlbumParser


class MockPagesScraper(PageScraper):
    def __init__(self, album_parser: AlbumParser, albums=None, num_pages=0):
        self._albums = albums
        self._page = None
        self._num_pages = num_pages

    def set_page(self, page):
        self._page = page

    @property
    def albums(self):
        return self._albums

    @property
    def num_pages(self):
        return self._num_pages


