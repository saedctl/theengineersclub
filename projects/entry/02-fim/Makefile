.PHONY: install test run-baseline run-check clean

install:
	pip install -r requirements.txt

test:
	python -m pytest tests/ -v

run-baseline:
	python src/main.py baseline --path ./sample_dir

run-check:
	python src/main.py check --path ./sample_dir

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
