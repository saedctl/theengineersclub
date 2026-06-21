.PHONY: install test run clean

install:
	pip install -r requirements.txt

test:
	python -m pytest tests/ -v

run:
	python src/main.py check "P@ssw0rd123" --wordlist --hibp

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
