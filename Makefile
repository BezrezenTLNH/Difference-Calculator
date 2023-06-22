install:
	poetry install

test:
	poetry run pytest

check:
	poetry check

lint:
	poetry run flake8 gendiff

build: check
	poetry build

lint:
	poetry run flake8 gendiff

