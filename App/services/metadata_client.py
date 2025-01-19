from abc import ABC, abstractmethod


class MetadataClient(ABC):



    @abstractmethod
    def search_album(self, title: str, artist: str) -> dict:
        pass

    @abstractmethod
    def search_artist(self, artist: str) -> dict:
        pass



