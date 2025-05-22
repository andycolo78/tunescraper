import argparse
from argparse import Namespace

from App.init.containers import ScraperContainer
from dependency_injector.wiring import Provide, inject
from App.tunescraper_app import TunescraperApp

'''
tunescraper : get the list of new music releases from websites and lists links to spotify
- scraping latest release data from albumoftheyear.org

'''

container = ScraperContainer()

@inject
def main(tune_scraper: TunescraperApp = Provide[ScraperContainer.tune_scraper]) -> None:
    parser = argparse.ArgumentParser(description="Find new music releases")
    parser.add_argument("-o", "--output", action="store_true", help="Print results to console output")
    parser.add_argument("-db", "--database", action="store_true", help="Save data to database")

    args =  parser.parse_args()

    releases = tune_scraper.get_releases()

    if args.database:
        print('Saved to DB')
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

def process_args() -> Namespace:
    parser = argparse.ArgumentParser(description="Find new music releases")
    parser.add_argument("-o", "--output", action="store_true", help="Print results to console output")
    parser.add_argument("-db", "--database", action="store_true", help="Save data to database")

    return parser.parse_args()
