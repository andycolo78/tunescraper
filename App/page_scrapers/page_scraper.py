from bs4 import BeautifulSoup

from App.locators.page_locators import PageLocators
from App.parsers.release_parser import ReleaseParser


class PageScraper:
    def __init__(self, release_parser: ReleaseParser):
        self._soup = None
        self._release_parser = release_parser

    def set_page(self, page: str) -> None:
        self._soup = BeautifulSoup(page, 'html.parser')

    @property
    def releases(self):
        releases = []
        for release_section in self._soup.select(PageLocators.RELEASES):
            self._release_parser.set_release_section(release_section)
            releases.append(self._release_parser.release)

        return releases

    @property
    def num_pages(self):
        last_page_element = self._soup.select_one(PageLocators.LAST_PAGE_NUMBER)
        return int(last_page_element.text)


