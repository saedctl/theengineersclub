.PHONY: install test run-scan-mock run-list clean

install:
	pip install -r requirements.txt

test:
	python -m pytest tests/ -v

run-scan-mock:
	python src/main.py scan --target mock --framework cis-aws --output report.md --format markdown

run-list:
	python src/main.py list --framework cis-aws

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -f report.md report.html
