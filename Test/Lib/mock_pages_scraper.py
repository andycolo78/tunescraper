from App.page_scrapers.page_scraper import PageScraper


class MockPagesScraper(PageScraper):
    def __init__(self, page_content, albums):
        self.page_content = page_content
        self._albums = albums

    def set_page(self, page):
        pass

    @property
    def albums(self):
        return self._albums
