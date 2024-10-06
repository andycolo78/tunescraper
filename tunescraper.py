from App.tunescraper import Tunescraper
from App.page_scrapers.page_scraper import PageScraper
from App.parsers.album_parser import AlbumParser
from App.services.chromedriver_requests_client import ChromedriverRequestsClient

from App.sites.aoty.aoty_config import AotyConfig

'''
tunescraper : get the list of new music releases from websites and lists links to spotify
- scraping latest release data from albumoftheyear.org

'''


def main(tune_scraper: Tunescraper) -> None:
    for release in tune_scraper.get_releases():
        print(f"{release['title'][:45] + "..." if len(release['title']) > 45 else release['title']:-<50} "
              f"{release['author']:<20}")


def get_url() -> str:
    return AotyConfig.URL


if __name__ == "__main__":
    main(Tunescraper(get_url(), PageScraper(AlbumParser()), ChromedriverRequestsClient()))
