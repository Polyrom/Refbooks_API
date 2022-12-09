start:
	poetry run python manage.py runserver

makemigrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

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

secretkey:
	poetry run python -c 'from django.utils.crypto import get_random_string; print(get_random_string(40))'
