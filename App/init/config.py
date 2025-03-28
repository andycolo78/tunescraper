from dataclasses import dataclass
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv(override=False)

@dataclass
class Config:
    """
        Data class used to store configuration constants
    """

    SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
    SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
    LOG_LEVEL = os.getenv("LOG_LEVEL")
    DEV_ENABLE = os.getenv("DEV_ENABLE").upper() == 'TRUE'

    DB_DRIVER=os.getenv("DB_DRIVER")
    DB_USER=os.getenv("DB_USER")
    DB_PASSWORD=os.getenv("DB_PASSWORD")
    DB_HOST=os.getenv("DB_HOST")
    DB_PORT=os.getenv("DB_PORT")
    DB_NAME=os.getenv("DB_NAME")

