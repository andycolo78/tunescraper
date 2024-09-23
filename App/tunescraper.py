import requests


class Tunescraper:

    def get_releases(self):
        pass

    def _get_page_content(self, url: str):
        page_content = requests.get(url).content
        print(page_content)
        return page_content

    def _get_albums_from_page(self, page):
        pass
