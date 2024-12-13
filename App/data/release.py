from dataclasses import dataclass


@dataclass
class Release:
    """
    Class to store album metadata
    """

    title: str = None
    author: str = None
    url: str = None
    genres: list[str] = None
    type: str = 'album'



