.PHONY: install test run-sync run-query run-api clean

install:
	pip install -r requirements.txt

test:
	python -m pytest tests/ -v

run-sync:
	python src/main.py sync --feeds urlhaus,feodo

run-query:
	python src/main.py query 1.2.3.4

run-api:
	uvicorn src.api:app --reload --port 8000

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -f threatfeed.db
