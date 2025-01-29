.DEFAULT_GOAL: run

run:
	cd app;	poetry run python run.py

install: pyproject.toml
	poetry install --no-root

check:
	poetry run flake8 src