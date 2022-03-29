install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/hexlet_code-0.1.0-py3-none-any.whl

make lint:
	poetry run flake8 brain_games
