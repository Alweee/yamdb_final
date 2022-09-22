# YaMDb

Проект YaMDb собирает отзывы `(Review)` пользователей на произведения `(Title)`. Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список категорий `(Category)` может быть расширен администратором. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку. В каждой категории есть произведения: книги, фильмы или музыка. Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Насекомые» и вторая сюита Баха. Произведению может быть присвоен жанр `(Genre)` из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). Новые жанры может создавать только администратор.

### Адрес сервера с приложением: `158.160.9.63`

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

`docker-compose exec web python manage.py migrate`

**Заполнить базу данными:**

`docker-compose exec web python manage.py loaddata fixtures.json`

**Создать суперпользователя:**

`docker-compose exec web python manage.py createsuperuser`

**Собрать статику:**

`docker-compose exec web python manage.py collectstatic --no-input`

### Примеры запросов:

**`GET` | Получение списка всех жанров: `/api/v1/genres/`**

Response:
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

**`POST` | Добавление произведения: `/api/v1/titles/`**

Request:
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
Response:
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
