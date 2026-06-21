# The Engineers Club — Security Engineering Projects

Hands-on security engineering projects for people building careers in cybersecurity. 15 projects across three levels, from log parsing to adversary simulation.

Built for the community at [theengineers.club](https://theengineers.club).

## Levels

| Level | Directory | Who it's for | Projects |
|-------|-----------|--------------|----------|
| Entry | [`projects/entry/`](projects/entry/) | Getting started with Python + security fundamentals | 5 |
| Mid | [`projects/mid/`](projects/mid/) | Integrating tools, building real pipelines | 5 |
| Senior | [`projects/senior/`](projects/senior/) | Architecture-level systems and advanced tooling | 5 |

## Project Index

| # | Level | Project | Description |
|---|-------|---------|-------------|
| 1 | Entry | [Log Sentinel](projects/entry/01-log-sentinel/) | Parse auth/syslog/nginx logs, detect brute-force and sudo abuse with threshold engine |
| 2 | Entry | [File Integrity Monitor](projects/entry/02-fim/) | Walk directories, SHA-256 hash files, store baselines, detect changes |
| 3 | Entry | [CVE CLI](projects/entry/03-cve-cli/) | Query the NVD API for CVEs with keyword search, severity filtering, and rich output |
| 4 | Entry | [Port Scanner](projects/entry/04-portscan/) | Multi-threaded TCP connect scanner with banner grabbing and service fingerprinting |
| 5 | Entry | [Password Auditor](projects/entry/05-passaudit/) | Entropy scoring, pattern detection, and HIBP breach checking for passwords |
| 6 | Mid | [SIEM Lite](projects/mid/01-siem-lite/) | Log ingestion pipeline with ECS normalisation, YAML correlation rules, and SQLite backend |
| 7 | Mid | [Threat Feed](projects/mid/02-threatfeed/) | Aggregate IOCs from OTX, AbuseIPDB, URLhaus, Feodo Tracker with FastAPI query endpoint |
| 8 | Mid | [Vulnerability Pipeline](projects/mid/03-vulnpipe/) | Wrap Nmap/Trivy/Grype, normalise findings, deduplicate, and generate Jinja2 reports |
| 9 | Mid | [IR Playbook Engine](projects/mid/04-ir-playbook/) | YAML-driven incident response automation with step executors and audit logging |
| 10 | Mid | [Secret Scanner](projects/mid/05-secretscan/) | Detect leaked secrets in code and git history using regex and entropy analysis |
| 11 | Senior | [Detection Engine](projects/senior/01-detect-engine/) | Sigma rule compiler targeting SQL, Elasticsearch DSL, and Splunk SPL with test harness |
| 12 | Senior | [EDR Agent](projects/senior/02-edr-agent/) | Host-based agent monitoring processes, network, and file events with YARA matching |
| 13 | Senior | [Adversary Simulator](projects/senior/03-advsim/) | MITRE ATT&CK-mapped TTP execution with scenario runner and detection coverage reporter |
| 14 | Senior | [AI Threat Hunter](projects/senior/04-ai-hunter/) | LLM-assisted threat hunting — natural language to SQL over DuckDB event store via Claude |
| 15 | Senior | [GRC Audit](projects/senior/05-grc-audit/) | Infrastructure compliance scanner for CIS, NIST, and SOC 2 with gap reporting |

## Getting started

Each project is self-contained. Pick one, install its dependencies, and start building.

```bash
# Clone the repo
git clone https://github.com/saedctl/theengineersclub.git
cd theengineersclub

# Pick a project
cd projects/entry/01-log-sentinel

# Install dependencies
make install
# or: pip install -r requirements.txt

# Run the stub (you'll see TODOs to implement)
python src/main.py --help

# Run tests
make test
```

## Project structure

Every project follows the same layout:

```
projects/[level]/[nn]-[project-name]/
├── README.md          # What to build, why it matters, how to run it
├── src/
│   ├── __init__.py
│   └── main.py        # CLI stub with argparse, subcommands, and TODO comments
├── tests/
│   └── test_main.py   # Placeholder tests with specific TODO items
├── requirements.txt   # Pinned dependencies
└── Makefile           # install / test / run targets
```

Some projects include additional starter files (YAML rules, playbooks, control definitions) where they add real scaffolding value.

## How these projects work

Each project gives you:

- A **working CLI stub** with argparse subcommands and flags already wired up
- **TODO comments** in `main.py` telling you exactly what to implement in each function
- **Placeholder tests** in `test_main.py` with specific test cases described as TODOs
- **Real dependencies** pinned in `requirements.txt`
- A **README** explaining what the tool does, why it matters for your career, and stretch goals

The stubs run but don't do anything yet. Your job is to replace the `NotImplementedError` calls with real implementations.

## Contributing

These projects are intentionally incomplete — that's the point. The value is in building them yourself.

If you want to contribute:

- Fix bugs in the scaffolding (broken imports, wrong CLI flags, etc.)
- Improve TODO descriptions to be clearer or more specific
- Add new starter files (fixture data, config examples, templates)
- Suggest new projects by opening an issue

Do not submit completed implementations. The learning happens in the building.
