import unittest

from App.page_scrapers.page_scraper import PageScraper


class PageScraperTest(unittest.TestCase):

    def test_set_page(self):
        with open('../Dataset/test_get_album_from_page.html', 'r') as file:
            page = file.read()

        page_scraper = PageScraper()
        page_scraper.set_page(page)

        self.assertEqual(page, page_scraper._page)

