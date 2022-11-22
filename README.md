# How install
$ sudo apt-get update

$ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
# How run
- add you data to .env

$ docker-compose up

# Что делает сервис?
Поднимает 3 docker container: posgSQL, MinIO, generate-image. 

## postSQL
Контейнер базы данных postSQL. Хранит навазние сохраненой картинки, ссылку на нее в MinIO, дату сохранения картинки.

## MinIO
Контейрен s3-like хранилища. Хранит картинки.

## generate-image
Python контейнер. Выполнят get запросы к сервисы со случаными картинками, сохраняет картинки в minIO, добавляет запись в базу данных о сохраненой картинке. 

# .env 
## minIO
- BUCKET - название хранилища.
- MINIO_HOST - адрес сервера minIO. (:MINIO_CONSOLE_PORT)
- MINIO_ROOT_USER - имя root пользователя (так же access key).
- MINIO_ROOT_PASSWORD- пароль для root пользователя (так же secret key).
- MINIO_API_PORT - порт для работы с api.
- MINIO_CONSOLE_PORT - порт для работы с консолью.
## psql

- DATABASE - имя базы данных.
- DB_USER - имя пользователя.
- DB_PASSWORD - пароль для пользователя .
- DB_HOST - адрес сервера базы данных.
- DB_PORT - порт базы данных.

## generate-image
- COUNT - количество get запросов для получения случаной картинки.
