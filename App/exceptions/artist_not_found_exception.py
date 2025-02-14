class ArtistNotFoundException(Exception):
    """This exception is raised when artist metadata are not found inside metadata client answer."""
    def __init__(self, message="Artist metadata not found", metadata=None):
        self.message = message
        super().__init__(self.message)