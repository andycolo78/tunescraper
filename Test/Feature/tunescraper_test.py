import unittest
import requests

from unittest import mock
from App.tunescraper import Tunescraper


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, page, status_code):
            self.content = page
            self.status_code = status_code

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

