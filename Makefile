#Makefile
# .PHONY: gendiff

install:
	poetry install

gen-diff:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

# make lint:
# 	poetry run flake8 gendiff

# make test:
# 	poetry run pytest

check:
	poetry run flake8 gendiff
	poetry run pytest

test-coverage:
	coverage run --source=. -m pytest
	coverage report
	coverage xml

