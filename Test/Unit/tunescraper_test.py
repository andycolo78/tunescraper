import unittest
from unittest.mock import MagicMock
from Test.Lib.mock_response import MockResponse
from Test.Lib.mock_pages_scraper import MockPagesScraper

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

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_page_content(self, mock_get):
        url = 'https://www.albumoftheyear.org/releases/this-week/'

        tunescraper = Tunescraper(url, PageScraper(AlbumParser()))

        expected = '<html lang="en"><title>This Week\'s New Album Releases</title></html>'

        page = tunescraper._get_page_content()

        self.assertEqual(expected, page)

    def test_get_albums_from_page(self):
        with open('../Dataset/test_get_albums_from_page.html', 'r') as file:
            page = file.read()

        expected_albums = [
            {'author': 'Jamie xx', 'title': 'In Waves', 'type': 'album'},
            {'author': 'Katy Perry', 'title': '143', 'type': 'album'},
            {'author': 'Future', 'title': 'MIXTAPE PLUTO', 'type': 'album'},
            {'author': 'The Voidz', 'title': 'Like All Before You', 'type': 'album'},
            {'author': 'The Alchemist', 'title': 'The Genuine Articulate', 'type': 'album'}
        ]

        tunescraper = Tunescraper('http://someurl.com', MockPagesScraper(page, expected_albums))
        albums = tunescraper._get_albums_from_page(page)

        self.assertEqual(expected_albums, albums)
