import re

from bs4 import BeautifulSoup

from App.parsers.album_parser import AlbumParser
from App.locators.album_locators import AlbumLocators


class MockAlbumParser(AlbumParser):
    def __init__(self, mocked):
        self._album_section = None
        self._mocked = mocked

    def set_album_section(self, section: str) -> None:
        self._album_section = section

    @property
    def album(self) -> list:
        for title, album in self._mocked.items():
            if re.search(title, str(self._album_section)):
                return album
        return []
