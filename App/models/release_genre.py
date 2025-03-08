from sqlalchemy import Column, Integer, ForeignKey
from App.init.database import Base

class ReleaseGenre(Base):
    __tablename__ = "releases_genres"

    release_id = Column(Integer, ForeignKey("releases.id"), primary_key=True)
    genre_id = Column(Integer, ForeignKey("genres.id"), primary_key=True)