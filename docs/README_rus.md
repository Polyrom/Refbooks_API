[![linter](https://github.com/Polyrom/Refbooks_API/actions/workflows/linter.yml/badge.svg)](https://github.com/Polyrom/Refbooks_API/actions/workflows/linter.yml) [![tests](https://github.com/Polyrom/Refbooks_API/actions/workflows/tests.yml/badge.svg)](https://github.com/Polyrom/Refbooks_API/actions/workflows/tests.yml) [![Test Coverage](https://api.codeclimate.com/v1/badges/7551ecaf8b206118fb0f/test_coverage)](https://codeclimate.com/github/Polyrom/Refbooks_API/test_coverage) [![Maintainability](https://api.codeclimate.com/v1/badges/7551ecaf8b206118fb0f/maintainability)](https://codeclimate.com/github/Polyrom/Refbooks_API/maintainability)

### REST API для терминологических справочников

 **Стек**
+ Python 3.10
+ Django 4.1 / DRF 3.14
+ SQLite
+ Swagger (drf-yasg 1.21)

### Установка
**Склонируйте репозиторий**
```
git clone https://github.com/Polyrom/Refbooks_API.git
cd Refbooks_API
```
<details>
<summary><strong>Установка с помощью Poetry</strong></summary>
<br>
Если Poetry не установлен, информацию об установке можно найти 
<a href="https://python-poetry.org/docs/"><strong>здесь</strong></a>
<br>

1. Установите зависимости:

```
make install
```
2. Создайте и заполните файл .env:
```
make env
```

3. Реализуйте миграцию схемы БД и создайте суперпользователя:
```
make initial-migration
make superuser
```
</details>
<details>
<summary><strong>Установка с помощью venv</strong></summary>
<br>

1. Создайте и активируйте виртуальное окружение:

```
python3 -m venv venv
source venv/bin/activate
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
3. Создайте и заполните файл .env:
```
python contrib/env_generator.py
```
4. Реализуйте миграцию схемы БД и создайте суперпользователя:
```
python manage.py migrate --run-syncdb
python manage.py createsuperuser
```
</details>

**Теперь можно запустить проект на вашем хосте**

Если вы используете Poetry:
```
make start
```
Если вы используете venv:
```
python manage.py runserver
```
Заполнить БД можно с помощью стандартной панели администратора Django:

```
http://<your_localhost>/admin/
```
### Использование
Документация Swagger UI с доступными эндпоинтами, HTTP-методами и примерами:
```
http://<your_localhost>/docs/
```