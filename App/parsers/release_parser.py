from App.locators.release_locators import ReleaseLocators
from App.data.release import Release


class ReleaseParser:
    def __init__(self):
        self._release_section = None

    def set_release_section(self, section) -> None:
        self._release_section = section

    def _parse_release(self):
        return Release(
            author=self._parse_author(),
            title=self._parse_title(),
            type='album'
        )

    def _parse_title(self):
        item_link = self._release_section.select_one(ReleaseLocators.TITLE)
        return item_link.text

    def _parse_author(self):
        item_link = self._release_section.select_one(ReleaseLocators.AUTHOR)
        return item_link.text

    @property
    def release(self) -> Release:
        return self._parse_release()
