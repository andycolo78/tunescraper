from App.locators.album_locators import AlbumLocators


class AlbumParser:
    def __init__(self):
        self._album_section = None

    def set_album_section(self, section) -> None:
        self._album_section = section

    def _parse_album(self):
        return {
            'author': self._parse_author(),
            'title': self._parse_title(),
            'type': 'album'
        }

    def _parse_title(self):
        item_link = self._album_section.select_one(AlbumLocators.TITLE)
        return item_link.text

    def _parse_author(self):
        item_link = self._album_section.select_one(AlbumLocators.AUTHOR)
        return item_link.text

    @property
    def album(self) -> dict:
        return self._parse_album()



