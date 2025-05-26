from sqlalchemy.orm import Session

from App.data.release import Release
from App.models.release import Release as ReleaseModel

from datetime import datetime, timezone


class ReleasesDbRepository:

    def __init__(self, session:Session) :
        self.__session = session

    def update_releases(self, releases:list[Release]) -> None:
        for release in releases:
            self.__session.add(ReleaseModel(
                title = release.title,
                author = release.author,
                type = release.type,
                update_date = datetime.now(timezone.utc)
            ))
        self.__session.commit()





