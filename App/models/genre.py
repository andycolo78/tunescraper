from sqlalchemy import Column, Integer, String
from App.init.database import Base

class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, autoincrement=True)
    genre = Column(String, nullable=False)