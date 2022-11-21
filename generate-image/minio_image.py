"""A few functions for work with s3 minio."""

# I don't know how tests this file
# TODO make tests for it
import io
import logging
import os

import requests
from dotenv import load_dotenv
from minio import Minio

load_dotenv()
BUCKET = os.getenv('BUCKET')
MINIO_HOST = os.getenv("MINIO_HOST")
MINIO_ROOT_USER = os.getenv("MINIO_ROOT_USER")
MINIO_ROOT_PASSWORD = os.getenv("MINIO_ROOT_PASSWORD")


def get_client():
    """Gets minio client."""
    # connect to minio
    client = Minio(
        endpoint=MINIO_HOST,
        access_key=MINIO_ROOT_USER,
        secret_key=MINIO_ROOT_PASSWORD,
        secure=False

    )
    # check and create bucket
    found = client.bucket_exists(BUCKET)
    if not found:
        client.make_bucket(BUCKET)
    else:
        logging.info(f"Bucket '{BUCKET}' already exists")

    return client


def save_image_to_s3(uid: str, url: str, file_format: str = "png") -> tuple:
    """Saves images to minio s3.

    Args:
        uid: str - images id, name for file.
        url: str - images url for downloads.
        file_format: str - saved file format.

    Returns:
         tuple - url saved image in s3, save date.
    """
    # get image
    re = requests.get(url)
    # save image
    client = get_client()
    result = client.put_object(
        BUCKET, "{0}.{1}".format(uid, file_format),
        io.BytesIO(re.content),
        length=-1, part_size=10 * 1024 * 1024,
    )
    # get url saved image in s3
    url_save = client.presigned_get_object(
        BUCKET, result.object_name
    )
    return url_save, result.object_name, result.http_headers.get("Date")
