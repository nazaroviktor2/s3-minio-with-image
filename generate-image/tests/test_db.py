import datetime
from unittest import TestCase, main

import psycopg2

from db import save_img_to_db, init_database
import testing.postgresql


class DataBaseTest(TestCase):
    def setUp(self):
        self.postgresql = testing.postgresql.Postgresql()
        dsn = self.postgresql.dsn()
        init_database(
            database=dsn.get("database"),
            user=dsn.get("user"),
            password=dsn.get("user"),
            host=dsn.get("host"),
            port=dsn.get("port")
        )

    def test_save_img_to_db(self):
        dsn = self.postgresql.dsn()
        uid = "testUID"
        file_name = "testUID.png"
        time = datetime.datetime.now()
        id = save_img_to_db(uid, file_name, time,
                            database=dsn.get("database"),
                            user=dsn.get("user"),
                            password=dsn.get("user"),
                            host=dsn.get("host"),
                            port=dsn.get("port"))

        with psycopg2.connect(
                database=dsn.get("database"),
                user=dsn.get("user"),
                password=dsn.get("user"),
                host=dsn.get("host"),
                port=dsn.get("port")) as con:
            cur = con.cursor()
            cur.execute(f"select * from images WHERE id = {id}")
            self.assertEqual(cur.fetchall(), [(id, uid, uid, time)])

    def tearDown(self):
        self.postgresql.stop()


if __name__ == '__main__':
    main()
