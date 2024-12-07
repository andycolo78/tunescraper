from dependency_injector import containers, providers

from App.tunescraper_app import TunescraperApp
from App.page_scrapers.page_scraper import PageScraper
from App.parsers.album_parser import AlbumParser

from App.sites.aoty.aoty_config import AotyConfig

from App.services.chromedriver_requests_client import ChromedriverRequestsClient


class ScraperContainer(containers.DeclarativeContainer):

    config = providers.Configuration()

    album_parser = providers.Singleton(
        AlbumParser
    )

    page_scraper = providers.Singleton(
        PageScraper,
        album_parser
    )

    request_client = providers.Singleton(
        ChromedriverRequestsClient
    )

    tune_scraper = providers.Factory(
        TunescraperApp,
        AotyConfig.URL,
        page_scraper,
        request_client
    )

