[![linter](https://github.com/Polyrom/Refbooks_API/actions/workflows/linter.yml/badge.svg)](https://github.com/Polyrom/Refbooks_API/actions/workflows/linter.yml) [![tests](https://github.com/Polyrom/Refbooks_API/actions/workflows/tests.yml/badge.svg)](https://github.com/Polyrom/Refbooks_API/actions/workflows/tests.yml) [![Maintainability](https://api.codeclimate.com/v1/badges/7551ecaf8b206118fb0f/maintainability)](https://codeclimate.com/github/Polyrom/Refbooks_API/maintainability)

### REST API to handle reference books

 **Stack**:
+ Python 3.10
+ Django 4.1 / DRF 3.14
+ SQLite
+ Swagger

### Installation
1. Clone the repository
```
git clone https://github.com/Polyrom/Refbooks_API.git
cd refbooks
```
2. Install dependencies with **Poetry**

    2.1. If you don't have Poetry installed, here's the installation guide:
         **[Poetry installation](https://python-poetry.org/docs/)**
```
make install
```

3. Create an .env file
```
touch .env
```
4. Populate the .env file with the following values:
```
DEBUG=True
SECRET_KEY=your Django secret key (may be generated with 'make secretkey' command)
```

5. Finish installation
```
make makemigrations
make migrate
make superuser
```
6. Now can run the app on you localhost
```
make start
```

### Usage
Endpoints with available HTTP methods and parameters can be found
in Swagger documentation:
```
http://<your localhost>/swagger/
```