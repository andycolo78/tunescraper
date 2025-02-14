import logging
import logging.handlers
from logging import Logger
import os
from App.init.config import Config


class LoggerFactory:
    """A factory class for creating and configuring loggers with rotating file handler."""

    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    LOG_DIR = "logs"
    LOG_FILE = os.path.join(LOG_DIR, "app.log")
    MAX_SIZE = 5 * 1024 * 1024  # 5MB per log file
    BACKUP_COUNT = 3  # Keep last 3 log files
    LOG_LEVEL = Config.LOG_LEVEL

    @staticmethod
    def get_logger(name: str = "root", log_level=LOG_LEVEL) -> Logger:
        """Returns a configured logger instance."""

        # Ensure log directory exists
        if not os.path.exists(LoggerFactory.LOG_DIR):
            os.makedirs(LoggerFactory.LOG_DIR)

        logger = logging.getLogger(name)
        logger.setLevel(log_level)

        # Avoid adding duplicate handlers
        if logger.hasHandlers():
            return logger

        # Console Handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Rotating File Handler (size-based)
        file_handler = logging.handlers.RotatingFileHandler(
            LoggerFactory.LOG_FILE, maxBytes=LoggerFactory.MAX_SIZE, backupCount=LoggerFactory.BACKUP_COUNT
        )
        file_handler.setLevel(logging.DEBUG)

        # Formatter
        formatter = logging.Formatter(LoggerFactory.LOG_FORMAT)
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # Add Handlers
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        return logger
