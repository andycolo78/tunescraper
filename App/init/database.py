from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from App.init.config import Config


DATABASE = {
    'drivername': Config.DB_DRIVER,
    'database': Config.DB_NAME,
    'username': Config.DB_USER if Config.DB_USER else '',
    'password': Config.DB_PASSWORD if Config.DB_PASSWORD else '',
    'host': Config.DB_HOST if Config.DB_HOST else '',
    'port': Config.DB_PORT if Config.DB_PORT else ''
}

# Replace with your actual MySQL database URL
DATABASE_URL = str(URL.create(**DATABASE))

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()