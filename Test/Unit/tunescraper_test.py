import unittest
from unittest.mock import MagicMock
from Test.Lib.mock_response import MockResponse
from Test.Lib.mock_pages_scraper import MockPagesScraper

import requests

from unittest import mock
from App.tunescraper import Tunescraper


def mocked_requests_get(*args, **kwargs):
    if args[0] == 'https://www.albumoftheyear.org/releases/this-week/':
        return MockResponse('<html lang="en"><title>This Week\'s New Album Releases</title></html>', 200)

    return MockResponse(None, 404)


class TunescraperTest(unittest.TestCase):

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_page_content(self, mock_get):
        tunescraper = Tunescraper()

        expected = '<html lang="en"><title>This Week\'s New Album Releases</title></html>'

        url = 'https://www.albumoftheyear.org/releases/this-week/'
        page = tunescraper._get_page_content(url)

        self.assertEqual(expected, page)

    def test_get_albums_from_page(self):
        with open('../Dataset/test_get_album_from_page.html', 'r') as file:
            page = file.read()

        expected_albums = [
            {'author': 'Jamie xx', 'name': 'In Waves', 'type': 'album'},
            {'author': 'Katy Perry', 'name': '143', 'type': 'album'},
            {'author': 'Future', 'name': 'MIXTAPE PLUTO', 'type': 'album'},
            {'author': 'The Voidz', 'name': 'Like All Before You', 'type': 'album'},
            {'author': 'The Alchemist', 'name': 'The Genuine Articulate', 'type': 'album'}
        ]

        tunescraper = Tunescraper(MockPagesScraper(page, expected_albums))
        albums = tunescraper._get_albums_from_page(page)

        self.assertEqual(expected_albums, albums)
