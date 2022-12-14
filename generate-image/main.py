"""Main module uses all others, meant to be run."""

import logging
import os

from dotenv import load_dotenv

from db import init_database
from random_image import get_images_json, save_images

load_dotenv()
COUNT = int(os.getenv('COUNT'))


def init():
    """Initializes database, logging."""
    logging.basicConfig(encoding='utf-8', level=logging.INFO)
    init_database()


def main():
    images = get_images_json(COUNT)
    save_images(images)


if __name__ == '__main__':
    init()
    main()
