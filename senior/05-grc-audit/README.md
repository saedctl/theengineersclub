# GRC Audit

An infrastructure compliance scanner that evaluates systems against security frameworks like CIS Benchmarks, NIST 800-53, and SOC 2.

## What it is

GRC Audit collects configuration data from AWS (via boto3), Kubernetes clusters, and local systems, then evaluates it against a YAML-defined control library. Controls map to CIS Benchmarks, NIST 800-53, and SOC 2 requirements. The evaluator runs each control's check against the collected config and generates a gap report in markdown or HTML using Jinja2 templates. A mock mode lets you develop and test without real infrastructure.

Compliance is not optional — every company handling sensitive data faces audits. GRC engineers spend weeks manually checking controls against infrastructure. Building an automated scanner teaches you how compliance frameworks map to technical controls, how to collect evidence programmatically, and how to generate audit-ready reports.

## What you'll build

- Config collectors for AWS (boto3), Kubernetes (kubernetes client), and local system
- Mock mode for development and testing without real infrastructure
- YAML control library with CIS, NIST, and SOC 2 mappings
- Control evaluator that checks collected config against control requirements
- Jinja2 gap report generator (markdown and HTML)
- CLI with `scan` and `list` subcommands

## Skills developed

- Cloud API integration (AWS boto3, Kubernetes client)
- Compliance framework understanding (CIS, NIST, SOC 2)
- Policy-as-code design patterns
- YAML schema design for security controls
- Report generation for non-technical stakeholders

## How to run

```bash
cd senior/05-grc-audit
make install

# Run with mock data (no cloud credentials needed):
python src/main.py scan --target mock --framework cis-aws --output report.md --format markdown

# Run against real AWS:
python src/main.py scan --target aws --framework cis-aws --output report.html --format html

# List available frameworks and controls:
python src/main.py list --framework cis-aws
python src/main.py list --framework nist-800-53
```

## Stretch goals

- Add Azure and GCP collectors
- Implement control remediation suggestions with exact CLI commands or Terraform snippets
- Build a trend tracker that compares scan results over time
- Add exception management (mark controls as accepted risk with justification)
- Export findings in OSCAL (Open Security Controls Assessment Language) format
