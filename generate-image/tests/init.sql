CREATE TABLE  IF NOT EXISTS  images (

    id   serial PRIMARY KEY
                 UNIQUE
                 NOT NULL,
url varchar,
file_name varchar,
saved_date timestamp
);
