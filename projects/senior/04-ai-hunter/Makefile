.PHONY: install test run-ingest run-query run-chat clean

install:
	pip install -r requirements.txt

test:
	python -m pytest tests/ -v

run-ingest:
	python src/main.py ingest --file events.json --format json

run-query:
	python src/main.py query "Show me all failed SSH logins in the last 24 hours"

run-chat:
	python src/main.py chat

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -f events.duckdb
