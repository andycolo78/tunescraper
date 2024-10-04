from bs4 import BeautifulSoup

from App.locators.page_locators import PageLocators
from App.parsers.album_parser import AlbumParser


class PageScraper:
    def __init__(self, album_parser: AlbumParser):
        self._soup = None
        self._album_parser = album_parser

    def set_page(self, page: str) -> None:
        self._soup = BeautifulSoup(page, 'html.parser')

    @property
    def albums(self):
        albums = []
        for album_section in self._soup.select(PageLocators.ALBUMS):
            self._album_parser.set_album_section(album_section)
            albums.append(self._album_parser.album)

        return albums
