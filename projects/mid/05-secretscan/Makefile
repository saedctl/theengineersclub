.PHONY: install test run-repo run-file clean

install:
	pip install -r requirements.txt

test:
	python -m pytest tests/ -v

run-repo:
	python src/main.py repo --path .

run-file:
	python src/main.py file --path src/main.py

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
