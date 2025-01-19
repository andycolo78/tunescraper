import unittest

from App.data.release import Release
from App.page_scrapers.page_scraper import PageScraper
from Test.Lib.mock_metadata_repository import MockMetadataRepository
from Test.Lib.mock_releases_repository import MockReleasesRepository

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

        mocked_releases = [
            Release(author='Jamie xx', title='In Waves', type='album'),
            Release(author='Katy Perry', title='143', type='album'),
            Release(author='Future', title='MIXTAPE PLUTO', type='album'),
            Release(author='The Voidz', title='Like All Before You', type='album'),
            Release(author='The Alchemist', title='The Genuine Articulate', type='album')
        ]

        mocked_metadata_releases = [
            Release(author='Jamie xx', title='In Waves', type='album',
                    url='https://open.spotify.com/album/57MSBg5pBQZH5bfLVDmeuP',
                    genres=['electronica', 'future garage', 'indie soul', 'indietronica']),
            Release(author='Katy Perry', title='143', type='album',
                    url='https://open.spotify.com/album/3jxt1S4JtW4uFalBwlfehS',
                    genres=['pop']),
            Release(author='Future', title='MIXTAPE PLUTO', type='album',
                    url='https://open.spotify.com/album/4Zoxsc06EUHRf5GrJPJZ54',
                    genres=['atl hip hop', 'hip hop', 'rap', 'southern hip hop', 'trap']),
            Release(author='The Voidz', title='Like All Before You', type='album',
                    url='https://open.spotify.com/album/7h0Y4HcaDsuLnXeYmvY7ai',
                    genres=['modern alternative rock']),
            Release(author='The Alchemist', title='The Genuine Articulate', type='album',
                    url='https://open.spotify.com/album/3EzeDYzLp9bcuK162KVDMp',
                    genres=['alternative hip hop', 'drumless hip hop', 'hip hop',
                            'instrumental hip hop', 'west coast rap']),
        ]

        expected_releases = [
            Release(author='Jamie xx', title='In Waves', type='album',
                    url='https://open.spotify.com/album/57MSBg5pBQZH5bfLVDmeuP',
                    genres=['electronica', 'future garage', 'indie soul', 'indietronica']),
            Release(author='Katy Perry', title='143', type='album',
                    url='https://open.spotify.com/album/3jxt1S4JtW4uFalBwlfehS',
                    genres=['pop']),
            Release(author='Future', title='MIXTAPE PLUTO', type='album',
                    url='https://open.spotify.com/album/4Zoxsc06EUHRf5GrJPJZ54',
                    genres=['atl hip hop', 'hip hop', 'rap', 'southern hip hop', 'trap']),
            Release(author='The Voidz', title='Like All Before You', type='album',
                    url='https://open.spotify.com/album/7h0Y4HcaDsuLnXeYmvY7ai',
                    genres=['modern alternative rock']),
            Release(author='The Alchemist', title='The Genuine Articulate', type='album',
                    url='https://open.spotify.com/album/3EzeDYzLp9bcuK162KVDMp',
                    genres=['alternative hip hop', 'drumless hip hop', 'hip hop',
                            'instrumental hip hop', 'west coast rap']),
        ]

        mock_releases_repository = MockReleasesRepository(
            url='http://www.something',
            page_scraper=PageScraper(ReleaseParser()),
            requests_client=RequestsClient(),
            mocked=mocked_releases)

        mock_metadata_repository = MockMetadataRepository(mocked=mocked_metadata_releases)

        tunescraper = TunescraperApp(
            releases_repository=mock_releases_repository,
            metadata_repository=mock_metadata_repository
        )
        releases = tunescraper.get_releases()

        self.assertEqual(
            [release.__dict__ for release in expected_releases],
            [release.__dict__ for release in releases]
        )

