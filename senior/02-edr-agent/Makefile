.PHONY: install test run-collector run-agent clean

install:
	pip install -r requirements.txt

test:
	python -m pytest tests/ -v

run-collector:
	uvicorn src.collector:app --port 9000 --reload

run-agent:
	python src/main.py start --collector http://localhost:9000 --foreground

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
