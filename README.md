# Проект "YaMDb"
Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles). Произведения делятся на категории (Category), список которых  может быть расширен администратором.
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
В каждой категории есть произведения. Произведению может быть присвоен жанр (Genre) из списка предустановленных. Новые жанры может создавать только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы (Review) и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.

![](https://github.com/Alweee/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

### Cтек технологий:
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=008080)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat&logo=Django%20REST%20Framework&logoColor=56C0C0&color=008080)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=PostgreSQL&logoColor=56C0C0&color=008080)](https://www.postgresql.org/)
[![JWT](https://img.shields.io/badge/-JWT-464646?style=flat&color=008080)](https://jwt.io/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat&logo=NGINX&logoColor=56C0C0&color=008080)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat&logo=gunicorn&logoColor=56C0C0&color=008080)](https://gunicorn.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/)
[![Docker-compose](https://img.shields.io/badge/-Docker%20compose-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/)
[![Docker Hub](https://img.shields.io/badge/-Docker%20Hub-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/products/docker-hub)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat&logo=Yandex.Cloud&logoColor=56C0C0&color=008080)](https://cloud.yandex.ru/)

### Шаблон наполнения env-файла:
- DB_ENGINE=db_engine
- DB_NAME=db_name
- POSTGRES_USER=postgres_user
- POSTGRES_PASSWORD=postgres_password
- DB_HOST=db_host
- DB_PORT=db_port
- SECRET_KEY=secret_key

### Команды для запуска приложения в контейнерах:

**Запустить приложение в контейнерах:**

из директории infra/

`docker-compose up -d --build`

**Выполнить миграции:**

из директории infra/

`docker-compose exec web python manage.py migrate`

**Заполнить базу данными:**

из директории infra/

`python manage.py loaddata fixtures.json`

**Создать суперпользователя:**

из директории infra/

`docker-compose exec web python manage.py createsuperuser`

**Собрать статику:**

из директории infra/

`docker-compose exec web python manage.py collectstatic --no-input`

### Примеры запросов:

**`GET` | Получение списка всех жанров: `api/v1/genres/`**

Response samples:
```
[
    {
        "count": 0,
        "next": "string",
        "previous": "string",
        "results": [
            {
                "name": "string",
                "slug": "string"
            }, ...
        ]
}
]
```

**`POST` | Добавление произведения: `api/v1/titles/`**

Request samples:
```
{
    "name": "string",
    "year": "2022",
    "description": "string",
    "genre": [
        "string"
    ],
    "category": "string"
}
```
Response samples:
```
{
    "id": 0,
    "name": "string",
    "year": 0,
    "rating": 0,
    "description": "string",
    "genre": [
        {...}
    ],
    "category": {
        "name": "string",
        "slug": "string"
    }
}
```
Разработчики:

[Александр Воробьёв](https://github.com/Alweee/)

[Александр Золототрубов](https://github.com/zolototrubov/)

[Николай Ушаков](https://github.com/northishere78/)
