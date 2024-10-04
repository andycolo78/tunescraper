from App.page_scrapers.page_scraper import PageScraper
from App.parsers.album_parser import AlbumParser


class MockPagesScraper(PageScraper):
    def __init__(self, album_parser: AlbumParser, albums):
        self._albums = albums
        self._page = None

    def set_page(self, page):
        self._page = page

    @property
    def albums(self):
        return self._albums
