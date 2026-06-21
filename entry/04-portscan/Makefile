.PHONY: install test run clean

install:
	pip install -r requirements.txt

test:
	python -m pytest tests/ -v

run:
	python src/main.py scanme.nmap.org --ports 22,80,443 --threads 10

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
