import argparse
from argparse import Namespace

from App.init.containers.scraper_container import ScraperContainer
from dependency_injector.wiring import Provide, inject

from App.repositories.releases_db_repository import ReleasesDbRepository
from App.repositories.releases_repository import ReleasesRepository

'''
tunescraper : get the list of new music releases from websites and lists links to spotify
- scraping latest release data from albumoftheyear.org

'''

container = ScraperContainer()

def process_args() -> Namespace:
    parser = argparse.ArgumentParser(description="Find new music releases")
    parser.add_argument("-o", "--output", action="store_true", help="Print results to console output")
    parser.add_argument("-db", "--database", action="store_true", help="Save data to database")

    return parser.parse_args()


@inject
def main(
        releases_repository: ReleasesRepository = Provide[ScraperContainer.releases_repository],
        releases_db_repository: ReleasesDbRepository = Provide[ScraperContainer.releases_db_repository],
) -> None:
    args = process_args()

    releases = releases_repository.fetch_releases()

    if args.database:
        releases_db_repository.update_releases(releases)
        print("SAVED TO DB!")
        return

    if args.output:
        for release in releases:
            print(f"{release.title[:45] + "..." if len(release.title) > 45 else release.title:-<50} "
                  f"{release.author[:40] + "..." if len(release.author) > 40 else release.author:-<50} "
                  )
        return

    print('Choose one available option [-o/--output , -db/--database]')

if __name__ == "__main__":
    container.wire(modules=[__name__])
    main()
