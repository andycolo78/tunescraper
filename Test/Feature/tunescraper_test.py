import os
import unittest
import subprocess

from unittest.mock import MagicMock
from unittest.mock import patch
import sys
from io import StringIO

import pytest
from dotenv import load_dotenv

from Test.Lib.mock_metadata_client import MockMetadataClient
from Test.Lib.mock_requests_client import MockRequestsClient

from dependency_injector import providers

from alembic.config import Config
from alembic import command






def mock_request_client_response() -> dict:
    url = 'https://www.albumoftheyear.org/releases/this-week/'
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Dataset",
                             "test_get_releases_from_single_page.html")
    with open(file_path, 'r') as file:
        page = file.read()

    return {url: page}

def get_expected_list() -> list:
    return ['Jamie xx', 'In Waves', 'Katy Perry', '143', 'Future', 'MIXTAPE PLUTO', 'The Voidz',
             'Like All Before You', 'The Alchemist', 'The Genuine Articulate']


def setup_db() :
    env_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "testing.env")
    load_dotenv(dotenv_path=env_file_path, override=True)

    from App.init.config import Config as Appconfig

    Appconfig.DB_DRIVER

    ini_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..","alembic.ini")

    alembic_cfg = Config(ini_file_path)
    migrations_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..","App","migrations")
    alembic_cfg.set_main_option("script_location", migrations_path)
    command.upgrade(alembic_cfg, "head")


class TunescraperTest(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    @patch.object(sys, "argv", ["tunescraper", "-o"])
    def test_output_option(self, stdout):
        from tunescraper import main
        from App.init.containers import ScraperContainer

        container = ScraperContainer()
        container.request_client.override(providers.Singleton(MockRequestsClient, mock_request_client_response()))

        container.wire(modules=['tunescraper'])
        main()

        printed_message = stdout.getvalue().strip()

        self.assertTrue(all(found in printed_message for found in get_expected_list()))

    @patch.object(sys, "argv", ["tunescraper", "-db"])
    def test_database_option(self):
        setup_db()
        from tunescraper import main
        from App.init.containers import ScraperContainer

        container = ScraperContainer()
        container.request_client.override(providers.Singleton(MockRequestsClient, mock_request_client_response()))

        container.wire(modules=['tunescraper'])
        main()

        from App.init.database import engine

        with engine.connect() as connection:
            result = connection.execute("SELECT * FROM releases")
            releases = result.fetchall()

        self.assertTrue(releases)
