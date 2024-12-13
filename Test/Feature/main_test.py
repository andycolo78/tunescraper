import unittest
from io import StringIO
from unittest.mock import MagicMock, patch
from App.data.release import Release

from tunescraper import main


class MainTest(unittest.TestCase):

    def test_main_calls_tunescraper(self):
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_main(self, stdout):
        release_list = [
            Release(author='Nilüfer Yanya', title='My Method Actor', type='album'),
            Release(author='julie', title='my anti-aircraft friend', type='album'),
            Release(author='Floating Points', title='Cascade', type='album'),
            Release(author='Ginger Root', title='SHINBANGUMI', type='album')
        ]

        exp_out = ''
        for release in release_list:
            exp_out += (f"{release.title[:45] + "..." if len(release.title) > 45 else release.title:-<50} " +
                        f"{release.author:<20}\n")

        mocked_tunescraper = MagicMock()
        mocked_tunescraper.get_releases.return_value = release_list

        main(mocked_tunescraper)

        printed_message = stdout.getvalue()

        self.assertEqual(exp_out, printed_message)
