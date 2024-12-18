import unittest

from App.data.release import Release
from App.page_scrapers.page_scraper import PageScraper
from Test.Lib.mock_releases_repository import MockReleasesRepository
from Test.Lib.mock_pages_scraper import MockPagesScraper
from Test.Lib.mock_requests_client import MockRequestsClient

from App.tunescraper_app import TunescraperApp
from App.parsers.release_parser import ReleaseParser
from App.services.requests_client import RequestsClient


class TunescraperAppTest(unittest.TestCase):

    def test_get_releases(self):
        url = 'https://www.albumoftheyear.org/releases/this-week/'
        with open('../Dataset/test_get_releases_from_page.html', 'r') as file:
            page = file.read()

        url_2 = 'https://www.albumoftheyear.org/releases/this-week/2/'
        with open('../Dataset/test_get_releases_from_page_2.html', 'r') as file:
            page_2 = file.read()

        pages = {url: page, url_2: page_2}

        expected_releases = [
            Release(author='Jamie xx', title='In Waves', type='album'),
            Release(author='Katy Perry', title='143', type='album'),
            Release(author='Future', title='MIXTAPE PLUTO', type='album'),
            Release(author='The Voidz', title='Like All Before You', type='album'),
            Release(author='The Alchemist', title='The Genuine Articulate', type='album')
        ]

        tunescraper = TunescraperApp(MockReleasesRepository(
            url='http://www.something',
            page_scraper=PageScraper(ReleaseParser()),
            requests_client=RequestsClient(),
            mocked=expected_releases))
        releases = tunescraper.get_releases()

        self.assertEqual(expected_releases, releases)

