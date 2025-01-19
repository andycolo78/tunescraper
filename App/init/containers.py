from dependency_injector import containers, providers

from App.tunescraper_app import TunescraperApp
from App.page_scrapers.page_scraper import PageScraper
from App.parsers.release_parser import ReleaseParser
from App.repositories.releases_repository import ReleasesRepository
from App.repositories.metadata_repository import MetadataRepository

from App.sites.aoty.aoty_config import AotyConfig

from App.services.chromedriver_requests_client import ChromedriverRequestsClient
from App.services.spotify_metadata_client import SpotifyMetadataClient

from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()


class ScraperContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    release_parser = providers.Singleton(
        ReleaseParser
    )

    page_scraper = providers.Singleton(
        PageScraper,
        release_parser
    )

    request_client = providers.Singleton(
        ChromedriverRequestsClient
    )

    releases_repository = providers.Singleton(
        ReleasesRepository,
        AotyConfig.URL,
        page_scraper,
        request_client
    )

    metadata_client = providers.Singleton(
        SpotifyMetadataClient,
        Spotify(auth_manager=SpotifyClientCredentials(client_id=os.getenv("SPOTIFY_CLIENT_ID"),
                                                      client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"))
                )
    )

    metadata_repository = providers.Singleton(
        MetadataRepository,
        metadata_client
    )

    tune_scraper = providers.Factory(
        TunescraperApp,
        releases_repository,
        metadata_repository
    )
