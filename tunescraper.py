from App.init.containers import ScraperContainer
from dependency_injector.wiring import Provide, inject
from App.tunescraper_app import TunescraperApp

'''
tunescraper : get the list of new music releases from websites and lists links to spotify
- scraping latest release data from albumoftheyear.org

'''


@inject
def main(tune_scraper: TunescraperApp = Provide[ScraperContainer.tune_scraper]) -> None:
    for release in tune_scraper.get_releases():
        print(f"{release['title'][:45] + "..." if len(release['title']) > 45 else release['title']:-<50} "
              f"{release['author']:<20}")


if __name__ == "__main__":
    container = ScraperContainer()
    container.wire(modules=[__name__])
    main()
