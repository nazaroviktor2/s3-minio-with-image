"""A few functions for work with image."""

import logging

import requests

from db import save_img_to_db
from minio_image import save_image_to_s3
from exceptions import InvalidImageFormat

URL_RANDOM_IMG = "https://random-data-api.com/api/placeholdit/random_placeholdit?size="


def get_images_json(count: int = 10) -> list:
    """Gets list of some count of images in json.

    Args:
        count: int - count images.

    Returns:
        list - images in json.

    Raises:
        TypeError: if count is not int.
    """
    if not isinstance(count, int):
        raise TypeError("Count must be integer, not {0}".format(type(int)))

    url = "{0}{1}".format(URL_RANDOM_IMG, count)
    return requests.get(url).json()


def save_images(images: list) -> None:
    """Saves images in s3 and saves information in db.

    Args:
        images: list - of image in json.
    """
    for image in images:
        try:
            save_image(image)
        except InvalidImageFormat as error:
            logging.error("Image can't be saved.")
            logging.error(str(error))


def save_image(image: dict):
    """Saves image in s3 and saves information in db.

    Args:
        image: dict - image to save.

    Raises:
        InvalidImageFormat: if image doesn't have parameters uid and image.
    """
    if not("uid" in image.keys() and "image" in image.keys()):
        raise InvalidImageFormat("Image musts have parameters uid and image.")

    uid = image.get("uid")
    url = image.get("image")
    s3_url, file_name, date_save = save_image_to_s3(uid, url)

    logging.info(f"{s3_url} save at {date_save}")
    save_img_to_db(s3_url, file_name, date_save)
