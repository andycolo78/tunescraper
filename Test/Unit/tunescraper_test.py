import unittest
from unittest.mock import MagicMock
from Test.Lib.mock_response import MockResponse
from Test.Lib.mock_pages_scraper import MockPagesScraper
from Test.Lib.mock_requests_client import MockRequestsClient

import requests

from unittest import mock
from App.tunescraper import Tunescraper
from App.page_scrapers.page_scraper import PageScraper
from App.parsers.album_parser import AlbumParser


def mocked_requests_get(*args, **kwargs):
    if args[0] == 'https://www.albumoftheyear.org/releases/this-week/':
        return MockResponse('<html lang="en"><title>This Week\'s New Album Releases</title></html>', 200)

    return MockResponse(None, 404)


class TunescraperTest(unittest.TestCase):

    def test_get_releases(self):
        url = 'https://www.albumoftheyear.org/releases/this-week/'
        with open('../Dataset/test_get_albums_from_page.html', 'r') as file:
            page = file.read()

        expected_albums = [
            {'author': 'Jamie xx', 'title': 'In Waves', 'type': 'album'},
            {'author': 'Katy Perry', 'title': '143', 'type': 'album'},
            {'author': 'Future', 'title': 'MIXTAPE PLUTO', 'type': 'album'},
            {'author': 'The Voidz', 'title': 'Like All Before You', 'type': 'album'},
            {'author': 'The Alchemist', 'title': 'The Genuine Articulate', 'type': 'album'}
        ]

        tunescraper = Tunescraper(url, MockPagesScraper(AlbumParser(), expected_albums), MockRequestsClient(page))
        albums = tunescraper.get_releases()

        self.assertEqual(expected_albums, albums)
