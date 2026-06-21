.PHONY: install test run-compile run-test run-validate clean

install:
	pip install -r requirements.txt

test:
	python -m pytest tests/ -v

run-compile:
	python src/main.py compile --rule src/rules/ssh_brute_force.yaml --backend sql

run-test:
	python src/main.py test --rule src/rules/ssh_brute_force.yaml --fixtures tests/fixtures/

run-validate:
	python src/main.py validate --rules-dir src/rules/

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
