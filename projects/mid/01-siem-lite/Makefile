.PHONY: install test run-ingest run-rules run-alerts clean

install:
	pip install -r requirements.txt

test:
	python -m pytest tests/ -v

run-ingest:
	python src/main.py ingest --source /var/log/auth.log --format syslog

run-rules:
	python src/main.py rules --run

run-alerts:
	python src/main.py alerts --last 20

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -f siem.db
