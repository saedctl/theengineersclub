# Vulnerability Pipeline

A unified vulnerability scanning pipeline that wraps multiple scanners and produces consolidated reports.

## What it is

VulnPipe orchestrates multiple vulnerability scanners (Nmap, Trivy, Grype) as subprocesses, parses their XML/JSON output into a common finding schema, deduplicates findings across scanners, and generates consolidated Jinja2-templated reports in markdown or HTML.

DevSecOps engineers spend significant time wrangling output from different scanners that all report on the same vulnerabilities in different formats. Building a unification pipeline teaches you how scanner output formats differ, why deduplication matters, and how to build reporting that actually gets read by engineering teams.

## What you'll build

- Scanner wrappers for Nmap, Trivy, and Grype as subprocess calls
- XML/JSON output parsers for each scanner
- Common finding schema (cve_id, package, version, fixed_in, cvss_score, epss_score, severity, scanner, target)
- Cross-scanner deduplication by CVE ID
- Jinja2 template engine for markdown and HTML reports
- CLI with `scan` and `report` subcommands

## Skills developed

- Subprocess management and output parsing
- XML and JSON parsing at scale
- Data normalisation across heterogeneous sources
- Template-based report generation with Jinja2
- CVSS and EPSS score interpretation
- DevSecOps pipeline design

## How to run

```bash
cd mid/03-vulnpipe
make install
python src/main.py scan --target myapp:latest --mode container
python src/main.py scan --target 192.168.1.0/24 --mode network
python src/main.py report --input findings.json --output report.md --format markdown
python src/main.py report --input findings.json --output report.html --format html
```

## Stretch goals

- Add EPSS score enrichment from the FIRST API to prioritise exploitable vulns
- Implement delta reports (what's new since last scan)
- Add a `--ci` mode that exits with non-zero status if critical vulns are found
- Integrate with Jira or GitHub Issues to auto-create tickets for new findings
- Add SLA tracking (days since CVE published vs. days unpatched)
