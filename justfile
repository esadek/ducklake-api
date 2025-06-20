alias fmt := format

default: format check

run:
    uv run src/ducklake_api/main.py

dev:
    uv run fastapi dev src/ducklake_api/main.py

test:
    uv run pytest

test-all-versions:
    uv run nox

check:
    uv run ruff check --fix
    uv run mypy .

format:
    uv run ruff format

clean:
    find . -type d -name '__pycache__' -exec rm -rf {} +
    rm -rf .venv
    rm -rf .ruff_cache
    rm -rf .mypy_cache
    rm -rf .pytest_cache
    rm -rf .nox
