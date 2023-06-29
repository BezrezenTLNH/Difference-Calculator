install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

coverage-missing:
	poetry run pytest --cov-report term-missing --cov=gendiff

flake8:
	pip install flake8
	poetry run flake8 gendiff

selfcheck:
	poetry check

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --force-reinstall --user dist/hexlet_code-0.1.0-py3-none-any.whl

check: selfcheck test lint

build:
	poetry build

.PHONY: install test lint selfcheck check build
