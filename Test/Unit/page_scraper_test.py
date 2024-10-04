import unittest
from bs4 import BeautifulSoup

from App.page_scrapers.page_scraper import PageScraper

from Test.Lib.mock_album_parser import MockAlbumParser


class PageScraperTest(unittest.TestCase):

    def test_set_page(self):
        with open('../Dataset/test_get_albums_from_page.html', 'r') as file:
            page = file.read()

        page_scraper = PageScraper(MockAlbumParser())
        page_scraper.set_page(page)

        self.assertIsInstance(page_scraper._soup, BeautifulSoup)

    def test_albums(self):
        with open('../Dataset/test_get_albums_from_page.html', 'r') as file:
            page = file.read()

        expected_albums = [
            {'author': 'Jamie xx', 'title': 'In Waves', 'type': 'album'},
            {'author': 'Katy Perry', 'title': '143', 'type': 'album'},
            {'author': 'Future', 'title': 'MIXTAPE PLUTO', 'type': 'album'},
            {'author': 'The Voidz', 'title': 'Like All Before You', 'type': 'album'},
            {'author': 'The Alchemist', 'title': 'The Genuine Articulate', 'type': 'album'}
        ]

        mocked_albums = {
            'In Waves': {'author': 'Jamie xx', 'title': 'In Waves', 'type': 'album'},
            '143': {'author': 'Katy Perry', 'title': '143', 'type': 'album'},
            'MIXTAPE PLUTO': {'author': 'Future', 'title': 'MIXTAPE PLUTO', 'type': 'album'},
            'Like All Before You': {'author': 'The Voidz', 'title': 'Like All Before You', 'type': 'album'},
            'The Genuine Articulate': {'author': 'The Alchemist', 'title': 'The Genuine Articulate', 'type': 'album'}
        }

        page_scraper = PageScraper(MockAlbumParser(mocked_albums))
        page_scraper.set_page(page)
        albums = page_scraper.albums

        self.assertEqual(expected_albums, albums)


