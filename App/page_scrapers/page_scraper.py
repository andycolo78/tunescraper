from App.locators.page_locators import PageLocators
from App.parsers.album_parser import AlbumParser


class PageScraper:
    def __init__(self, page_locators: PageLocators, album_parser: AlbumParser):
        self._page = None

    def set_page(self, page: str) -> None:
        self._page = page

    @property
    def albums(self):
        return self.albums

