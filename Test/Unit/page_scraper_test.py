import os
import unittest
from bs4 import BeautifulSoup

from App.data.release import Release
from App.page_scrapers.page_scraper import PageScraper
from App.parsers.release_parser import ReleaseParser

from Test.Lib.mock_release_parser import MockReleaseParser


class PageScraperTest(unittest.TestCase):

    def test_set_page(self):
        file_path = os.path.join(os.getcwd(), "..", "Dataset", "test_get_releases_from_page.html")
        with open(file_path, 'r') as file:
            page = file.read()

        page_scraper = PageScraper(MockReleaseParser({}))
        page_scraper.set_page(page)

        self.assertIsInstance(page_scraper._soup, BeautifulSoup)

    def test_releases(self):
        file_path = os.path.join(os.getcwd(), "..", "Dataset", "test_get_releases_from_page.html")
        with open(file_path, 'r') as file:
            page = file.read()

        expected_releases = [
            Release(author='Jamie xx', title='In Waves', type='album'),
            Release(author='Katy Perry', title='143', type='album'),
            Release(author='Future', title='MIXTAPE PLUTO', type='album'),
            Release(author='The Voidz', title='Like All Before You', type='album'),
            Release(author='The Alchemist', title='The Genuine Articulate', type='album')
        ]

        mocked_releases = {
            'In Waves': Release(author='Jamie xx', title='In Waves', type='album'),
            '143': Release(author='Katy Perry', title='143', type='album'),
            'MIXTAPE PLUTO': Release(author='Future', title='MIXTAPE PLUTO', type='album'),
            'Like All Before You': Release(author='The Voidz', title='Like All Before You', type='album'),
            'The Genuine Articulate': Release(author='The Alchemist', title='The Genuine Articulate', type='album')
        }

        page_scraper = PageScraper(MockReleaseParser(mocked_releases))
        page_scraper.set_page(page)
        releases = page_scraper.releases

        self.assertEqual(expected_releases, releases)

    def test_num_pages(self):
        file_path = os.path.join(os.getcwd(), "..", "Dataset", "test_get_releases_from_page.html")
        with open(file_path, 'r') as file:
            page = file.read()

        expected_num_pages = 2

        page_scraper = PageScraper(MockReleaseParser({}))
        page_scraper.set_page(page)
        num_pages = page_scraper.num_pages

        self.assertEqual(expected_num_pages, num_pages)
