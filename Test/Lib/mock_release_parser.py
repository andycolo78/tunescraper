import re
from App.parsers.release_parser import ReleaseParser


class MockReleaseParser(ReleaseParser):
    def __init__(self, mocked):
        self._release_section = None
        self._mocked = mocked

    def set_release_section(self, section: str) -> None:
        self._release_section = section

    @property
    def release(self) -> list:
        for title, release in self._mocked.items():
            if re.search(title, str(self._release_section)):
                return release
        return []
