class AlbumNotFoundException(Exception):
    """This exception is raised when album metadata are not found inside metadata client answer."""
    def __init__(self, message="Album metadata not found", metadata=None):
        self.message = message
        super().__init__(self.message)