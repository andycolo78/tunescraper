import unittest
from unittest.mock import MagicMock

from App.data.release import Release
from App.repositories.releases_db_repository import ReleasesDbRepository


class ReleasesDbRepositoryTest(unittest.TestCase):

    def test_update_releases(self):
        releases = [
            Release(author='Jamie xx', title='In Waves', type='album'),
            Release(author='Katy Perry', title='143', type='album'),
            Release(author='Future', title='MIXTAPE PLUTO', type='album'),
            Release(author='The Voidz', title='Like All Before You', type='album'),
            Release(author='The Alchemist', title='The Genuine Articulate', type='album')
        ]

        mock_db_session = MagicMock()
        mock_db_session.query.return_value.filter_by.return_value.first.side_effect = [None, None, None]

        releases_db_repository = ReleasesDbRepository(mock_db_session)
        releases_db_repository.update_releases(releases)
        self.assertEqual(mock_db_session.add.call_count, 5)
        self.assertTrue(mock_db_session.commit.called)




