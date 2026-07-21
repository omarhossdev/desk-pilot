default:
		@just --list

install:
    uv sync

lint:
		uv run ruff check --fix src/
		uv run ruff format src/

check: 
		uv run pyright src/

run: check
		uv run python src/main.py

