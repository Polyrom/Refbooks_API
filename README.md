[![linter](https://github.com/Polyrom/Refbooks_API/actions/workflows/linter.yml/badge.svg)](https://github.com/Polyrom/Refbooks_API/actions/workflows/linter.yml) [![tests](https://github.com/Polyrom/Refbooks_API/actions/workflows/tests.yml/badge.svg)](https://github.com/Polyrom/Refbooks_API/actions/workflows/tests.yml) [![Test Coverage](https://api.codeclimate.com/v1/badges/7551ecaf8b206118fb0f/test_coverage)](https://codeclimate.com/github/Polyrom/Refbooks_API/test_coverage) [![Maintainability](https://api.codeclimate.com/v1/badges/7551ecaf8b206118fb0f/maintainability)](https://codeclimate.com/github/Polyrom/Refbooks_API/maintainability)

### REST API to handle reference books

 **Stack**:
+ Python 3.10
+ Django 4.1 / DRF 3.14
+ SQLite
+ Swagger (drf-yasg 1.21)

### Installation
1. Clone the repository
```
git clone https://github.com/Polyrom/Refbooks_API.git
cd Refbooks_API
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
make migrate
make superuser
```
6. Now can run the app on your localhost
```
make start
```
7. You can populate the database through the standard Django admin
page at `http://<your localhost>/admin/
`
### Usage
Endpoints with available HTTP methods and parameters can be found
in Swagger documentation at `http://<your localhost>/docs/`