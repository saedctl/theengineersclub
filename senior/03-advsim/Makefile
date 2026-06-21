.PHONY: install test run-list run-technique run-scenario clean

install:
	pip install -r requirements.txt

test:
	python -m pytest tests/ -v

run-list:
	python src/main.py list

run-technique:
	python src/main.py run --technique T1059 --target localhost --dry-run

run-scenario:
	python src/main.py scenario --file src/scenarios/initial_access.yaml --dry-run

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
