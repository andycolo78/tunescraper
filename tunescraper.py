from App.tunescraper import Tunescraper

'''
tunescraper : get the list of new music releases from websites and lists links to spotify
- scraping latest release data from albumoftheyear.org

'''


def main(tune_scraper: Tunescraper) -> None:
    for release in tune_scraper.get_releases():
        print(f"{release['name']} - {release['author']}")


if __name__ == "__main__":
    main(Tunescraper())