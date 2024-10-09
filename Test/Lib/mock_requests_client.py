from App.services.requests_client import RequestsClient


class MockRequestsClient(RequestsClient):

    def __init__(self, responses: dict):
        self._responses = responses

    def get(self, url: str):
        return self._responses[url]



