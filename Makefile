#Makefile
# .PHONY: gendiff

install:
	poetry install

gen-diff:
	poetry run gendiff /home/larriva/python-project-50/tests/fixtures/file12.yml /home/larriva/python-project-50/tests/fixtures/file22.yml -f stylish

gen-diff-json:
	poetry run gendiff /home/larriva/python-project-50/tests/fixtures/file12.yml /home/larriva/python-project-50/tests/fixtures/file22.yml -f json

gen-diff-plain:
	poetry run gendiff /home/larriva/python-project-50/tests/fixtures/file12.yml /home/larriva/python-project-50/tests/fixtures/file22.yml -f plain

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

check:
	poetry run flake8 gendiff
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff tests/ --cov-report xml
