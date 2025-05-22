from sqlalchemy.orm import Session

from App.models.release import Release


class ReleasesDbRepository:

    def __init__(self, session:Session) :
        self.__session = session

    def update_releases(self, releases:list[Release]) -> None:
        for release in releases:
            self.__session.add(release)
        self.__session.commit()





