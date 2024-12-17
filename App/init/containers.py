from dependency_injector import containers, providers

from App.tunescraper_app import TunescraperApp
from App.page_scrapers.page_scraper import PageScraper
from App.parsers.release_parser import ReleaseParser
from App.repositories.releases_repository import ReleasesRepository

from App.sites.aoty.aoty_config import AotyConfig

from App.services.chromedriver_requests_client import ChromedriverRequestsClient


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

    tune_scraper = providers.Factory(
        TunescraperApp,
        releases_repository
    )

