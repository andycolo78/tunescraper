import undetected_chromedriver as uc

from App.page_scrapers.page_scraper import PageScraper


class Tunescraper:
    def __init__(self, url: str, page_scraper: PageScraper):
        self._page_scraper = page_scraper
        self._url = url

    def get_releases(self) -> list:
        page_content = self._get_page_content()
        return self._get_albums_from_page(page_content)

    def _get_page_content(self) -> str:
        driver = uc.Chrome()
        driver.get(self._url)
        page_content = driver.page_source
        return str(page_content)

    def _get_albums_from_page(self, page) -> list:
        self._page_scraper.set_page(page)
        return self._page_scraper.albums

