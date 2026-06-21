# Detection Engine

A Sigma rule compiler and testing framework that translates detection rules into multiple backend query languages.

## What it is

Detection Engine parses Sigma YAML detection rules into an internal AST model, then compiles them to backend-specific query languages — SQL (for SQLite/DuckDB), Elasticsearch DSL, and Splunk SPL. It includes a test harness that runs rules against fixture log data and reports true positives, false positives, and true negatives. A validation command checks all rules in a directory for syntax and logic errors.

Sigma is the open standard for detection rules, like YARA is for malware signatures. Security engineers write Sigma rules once and compile them to whatever SIEM they run. Building a compiler teaches you formal language translation, AST design, and the practical reality that every SIEM query language has different semantics for the same logical operation.

## What you'll build

- Sigma YAML rule parser into an internal detection model
- Backend compilers for SQL, Elasticsearch DSL, and Splunk SPL
- Test harness: run a rule against fixture log files, report TP/FP/TN
- Rule validator checking syntax and semantic correctness
- CLI with `compile`, `test`, and `validate` subcommands

## Skills developed

- Formal language parsing and AST design
- Multi-backend code generation (the compiler pattern)
- Detection engineering concepts (Sigma rule syntax, field mappings)
- Test harness design for security rules
- YAML schema validation

## How to run

```bash
cd projects/senior/01-detect-engine
make install
python src/main.py compile --rule src/rules/ssh_brute_force.yaml --backend sql
python src/main.py compile --rule src/rules/ssh_brute_force.yaml --backend elasticsearch
python src/main.py compile --rule src/rules/ssh_brute_force.yaml --backend splunk
python src/main.py test --rule src/rules/ssh_brute_force.yaml --fixtures tests/fixtures/
python src/main.py validate --rules-dir src/rules/
```

## Stretch goals

- Add field mapping configuration (Sigma field names to backend-specific field names)
- Implement rule chaining (rule A triggers, then rule B must fire within N seconds)
- Add a `--benchmark` flag to test compilation speed across backends
- Support Sigma modifiers (contains, startswith, endswith, re, base64)
- Build a web UI for rule authoring and live compilation preview
