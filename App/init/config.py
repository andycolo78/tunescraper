from dataclasses import dataclass
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

@dataclass
class Config:
    """
        Data class used to store configuration constants
    """

    SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
    SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
    LOG_LEVEL = os.getenv("LOG_LEVEL")
    DEV_ENABLE = os.getenv("DEV_ENABLE").upper() == 'TRUE'

