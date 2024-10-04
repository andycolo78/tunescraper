import unittest
from io import StringIO
from unittest.mock import MagicMock, patch

from tunescraper import main


class MainTest(unittest.TestCase):

    def test_main_calls_tunescraper(self):
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_main(self, stdout):

        release_list = [
            {'author': 'Nilüfer Yanya', 'title': 'My Method Actor', 'type': 'album'},
            {'author': 'julie', 'title': 'my anti-aircraft friend', 'type': 'album'},
            {'author': 'Floating Points', 'title': 'Cascade', 'type': 'album'},
            {'author': 'Ginger Root', 'title': 'SHINBANGUMI', 'type': 'album'}
        ]

        expected_output = ''
        for release in release_list:
            expected_output += f"{release['title']} - {release['author']}\n"

        mocked_tunescraper = MagicMock()
        mocked_tunescraper.get_releases.return_value = release_list

        main(mocked_tunescraper)

        printed_message = stdout.getvalue()

        self.assertEqual(expected_output, printed_message)

