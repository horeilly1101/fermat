"""File that contains the Config object."""
import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY") or "make sure to update this..."
    # add more config vars here
