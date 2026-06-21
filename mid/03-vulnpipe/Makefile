.PHONY: install test run-scan run-report clean

install:
	pip install -r requirements.txt

test:
	python -m pytest tests/ -v

run-scan:
	python src/main.py scan --target myapp:latest --mode container

run-report:
	python src/main.py report --input findings.json --output report.md --format markdown

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -f findings.json report.md report.html
