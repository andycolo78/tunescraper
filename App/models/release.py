from sqlalchemy import Column, Integer, String, DateTime
from App.init.database import Base


class Release(Base):
    __tablename__ = "releases"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(256), nullable=False)
    author = Column(String(256), nullable=False)
    type = Column(String(32), nullable=False)
    update_date = Column(DateTime, nullable=False)