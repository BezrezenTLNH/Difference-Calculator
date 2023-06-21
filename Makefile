install:
	poetry install

test:
	poetry run pytest

selfcheck:
	poetry check

lint:
	poetry run flake8 gendiff

build: check
	poetry build

