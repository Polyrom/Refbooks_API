start:
	poetry run python manage.py runserver

makemigrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

superuser:
	poetry run python manage.py createsuperuser

lint:
	poetry run flake8 api

update:
	poetry update

install:
	poetry install

shell:
	poetry run python manage.py shell

test:
	poetry run python manage.py test

test-coverage:
	poetry run coverage run manage.py test
	poetry run coverage xml
	poetry run coverage report

env:
	poetry run python contrib/env_generator.py

initial-migration:
	poetry run python manage.py migrate --run-syncdb
