import undetected_chromedriver

from App.services.requests_client import RequestsClient


class ChromedriverRequestsClient(RequestsClient):
    def __init__(self):
        self._driver = undetected_chromedriver.Chrome()

    def get(self, url: str) -> str:
        self._driver.get(url)
        page_content = self._driver.page_source
        return str(page_content)
