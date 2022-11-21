"""A few functions for work with database."""

import logging
import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()
DATABASE = os.getenv('DATABASE')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')


def save_img_to_db(url: str, file_name: str, save_date: str, database=DATABASE,
                   user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT):
    """Saves image saves information in db.

    Args:
        url: str - url to image in s3.
        file_name: str - file name in s3.
        save_date: str - when image was saved.
        database: str - name of database.
        user: str - login for connect to db.
        password: str - password for connect to db.
        host: str - host for connect to db.
        port: str - post for connect to db.
    """
    with psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port) as con:
        cur = con.cursor()

        cur.execute("INSERT INTO images (url,file_name, saved_date) VALUES (%s,%s, %s)  RETURNING id;",
                    (url, file_name, save_date))
        id = cur.fetchone()[0]
        logging.info(f"Image successfully registered in db with id = {id}")
        return id


def init_database(database=DATABASE, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT):
    """Initializes database.

    Args:
        database: str - name of database.
        user: str - login for connect to db.
        password: str - password for connect to db.
        host: str - host for connect to db.
        port: str - post for connect to db.
    """
    with psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port) as con:
        cur = con.cursor()
        with open("init.sql", "r") as file:
            cur.execute(file.read())
