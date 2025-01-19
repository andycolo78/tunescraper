from App.data.release import Release
from App.repositories.metadata_repository import MetadataRepository


class MockMetadataRepository(MetadataRepository):

    def __init__(self, mocked: list[Release]):
        super().__init__()
        self._mocked = mocked

    def add_metadata(self, releases: list[Release]) -> list[Release]:
        return self._mocked



