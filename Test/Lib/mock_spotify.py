from spotipy import Spotify


class MockSpotify(Spotify):

    def __init__(self, mocked_responses: dict):
        super().__init__()
        self._mocked_responses = mocked_responses

    def search(self, q, limit=10, offset=0, type="track", market=None):
        return self._mocked_responses[q]


