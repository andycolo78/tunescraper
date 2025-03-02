import os
import unittest

from App.data.release import Release
from Test.Lib.mock_response import MockResponse
from Test.Lib.mock_pages_scraper import MockPagesScraper
from Test.Lib.mock_requests_client import MockRequestsClient

from App.repositories.releases_repository import ReleasesRepository
from App.parsers.release_parser import ReleaseParser
from App.services.requests_client import RequestsClient


def mocked_requests_get(*args, **kwargs):
    if args[0] == 'https://www.albumoftheyear.org/releases/this-week/':
        return MockResponse('<html lang="en"><title>This Week\'s New Album Releases</title></html>', 200)

    return MockResponse(None, 404)


class ReleasesRepositoryTest(unittest.TestCase):

    def test_fetch_releases(self):
        url = 'https://www.albumoftheyear.org/releases/this-week/'
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Dataset",
                                 "test_get_releases_from_page.html")
        with open(file_path, 'r') as file:
            page = file.read()

        url_2 = 'https://www.albumoftheyear.org/releases/this-week/2/'
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Dataset",
                                 "test_get_releases_from_page_2.html")
        with open(file_path, 'r') as file:
            page_2 = file.read()

        pages = {url: page, url_2: page_2}

        expected_releases = [
            Release(author='Jamie xx', title='In Waves', type='album'),
            Release(author='Katy Perry', title='143', type='album'),
            Release(author='Future', title='MIXTAPE PLUTO', type='album'),
            Release(author='The Voidz', title='Like All Before You', type='album'),
            Release(author='The Alchemist', title='The Genuine Articulate', type='album')
        ]

        aoty_releases_repository = ReleasesRepository(url, MockPagesScraper(ReleaseParser(), expected_releases), MockRequestsClient(pages))
        releases = aoty_releases_repository.fetch_releases()

        self.assertEqual(
            [release.__dict__ for release in expected_releases],
            [release.__dict__ for release in releases]
        )

    def test_get_total_pages(self):
        url = 'https://www.albumoftheyear.org/releases/this-week/'
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Dataset",
                                 "test_get_releases_from_page.html")
        with open(file_path, 'r') as file:
            page = file.read()

        expected_num_pages = 2

        aoty_releases_repository = ReleasesRepository(url, MockPagesScraper(ReleaseParser(), num_pages=expected_num_pages), RequestsClient())
        num_pages = aoty_releases_repository._get_total_pages(page)

        self.assertEqual(expected_num_pages, num_pages)
