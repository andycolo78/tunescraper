import io
import os
import sys
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
            {'author': 'Nilüfer Yanya', 'name': 'My Method Actor', 'type': 'album'},
            {'author': 'julie', 'name': 'my anti-aircraft friend', 'type': 'album'},
            {'author': 'Floating Points', 'name': 'Cascade', 'type': 'album'},
            {'author': 'Ginger Root', 'name': 'SHINBANGUMI', 'type': 'album'}
        ]

        mocked_tunescraper = MagicMock()
        mocked_tunescraper.get_releases.return_value = release_list

        main(mocked_tunescraper)

        printed_message = stdout.getvalue().strip()

        self.assertEqual(f"{file_length} bytes {filename}", printed_message)

