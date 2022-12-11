[![linter](https://github.com/Polyrom/Refbooks_API/actions/workflows/linter.yml/badge.svg)](https://github.com/Polyrom/Refbooks_API/actions/workflows/linter.yml) [![tests](https://github.com/Polyrom/Refbooks_API/actions/workflows/tests.yml/badge.svg)](https://github.com/Polyrom/Refbooks_API/actions/workflows/tests.yml) [![Test Coverage](https://api.codeclimate.com/v1/badges/7551ecaf8b206118fb0f/test_coverage)](https://codeclimate.com/github/Polyrom/Refbooks_API/test_coverage) [![Maintainability](https://api.codeclimate.com/v1/badges/7551ecaf8b206118fb0f/maintainability)](https://codeclimate.com/github/Polyrom/Refbooks_API/maintainability)

### REST API to handle reference books

 **Stack**
+ Python 3.10
+ Django 4.1 / DRF 3.14
+ SQLite
+ Swagger (drf-yasg 1.21)

### Installation
**Clone the repository**
```
git clone https://github.com/Polyrom/Refbooks_API.git
cd Refbooks_API
```
<details>
<summary><strong>Installation guide using Poetry</strong></summary>
<br>
If you don't have Poetry installed, here's the installation guide:
         <a href="https://python-poetry.org/docs/"><strong>Poetry installation</strong></a>
<br>

1. Install dependencies

```
make install
```
2. Create and populate the .env file
```
make env
```

3. Migrate the DB and create supersuser
```
make initial-migration
make superuser
```
</details>
<details>
<summary><strong>Installation guide using standard venv</strong></summary>
<br>

1. Create and activate virtual environment

```
python3 -m venv venv
source venv/bin/activate
```
2. Install dependencies
```
pip install -r requirements.txt
```
3. Create and populate the .env file
```
python contrib/env_generator.py
```
4. Migrate the DB schema and create superuser
```
python manage.py migrate --run-syncdb
python manage.py createsuperuser
```
</details>

**Now you are ready to run the app on your localhost**

To get the server running with Poetry:
```
make start
```
To get the server running with venv:
```
python manage.py runserver
```
You can populate the database through the standard Django admin
page at

```
http://<your localhost>/admin/
```
### Usage
Endpoints with available HTTP methods and parameters can be found
in Swagger documentation at
```
http://<your localhost>/docs/
```