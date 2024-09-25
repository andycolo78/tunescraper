class MockResponse:
    def __init__(self, page, status_code):
        self.content = page
        self.status_code = status_code