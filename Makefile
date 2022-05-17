install:
	poetry install

lint:
	poetry run flake8 brain_games

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

publish:
	poetry publish --dry-run
