import logging

from fastapi import FastAPI
from pythonjsonlogger.json import JsonFormatter

LOGGING_FILE = "app.log"

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

logger_handler = logging.FileHandler(LOGGING_FILE)
logger_handler.setFormatter(
    JsonFormatter("{message}{levelname}", style="{", timestamp=True)
)
logger.addHandler(logger_handler)


app = FastAPI()


@app.get("/info")
def info():
    logger.info("Info message")


@app.get("/debug")
def debug():
    logger.debug("Debug message")
