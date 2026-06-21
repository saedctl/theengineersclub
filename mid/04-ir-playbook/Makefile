.PHONY: install test run-trigger run-dry-run run-list run-audit clean

install:
	pip install -r requirements.txt

test:
	python -m pytest tests/ -v

run-trigger:
	python src/main.py trigger --alert brute_force --data '{"source_ip": "1.2.3.4"}'

run-dry-run:
	python src/main.py trigger --alert brute_force --data '{"source_ip": "1.2.3.4"}' --dry-run

run-list:
	python src/main.py playbooks --list

run-audit:
	python src/main.py audit --last 20

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -f audit.log
