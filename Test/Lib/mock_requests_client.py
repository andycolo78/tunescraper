from App.services.requests_client import RequestsClient


class MockRequestsClient(RequestsClient):

    def __init__(self, response: str):
        self._response = response

    def get(self, url: str):
        return self._response

