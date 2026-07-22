default:
		@just --list

install:
                uv sync

lint:
		uv run ruff check --fix .
		uv run ruff format .

check: 
		uv run pyright src/

test:
		PYTHONPATH=. uv run pytest tests/ -v 

test-cov:
		PYTHONPATH=. uv run pytest --cov=src tests/ --cov-report=term-missing

run: check
		uv run python src/main.py

