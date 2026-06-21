# SIEM Lite

A lightweight Security Information and Event Management system with log ingestion, correlation rules, and alerting.

## What it is

SIEM Lite is a log ingestion and correlation pipeline. It accepts logs in multiple formats (syslog, JSON, CSV) through pluggable ingestors, normalises them to a common ECS-inspired event schema, stores them in SQLite, and evaluates YAML-defined correlation rules with time windows. When rules match, alerts are dispatched to a configurable webhook.

SIEMs are the central nervous system of any SOC. Products like Splunk, Elastic SIEM, and Sentinel cost six figures and require teams to operate, but the core concepts — normalisation, correlation, and alerting — are the same at every scale. Building a minimal SIEM teaches you what those products actually do under the hood.

## What you'll build

- Pluggable log ingestors for syslog, JSON, and CSV formats
- Event normalisation to a common ECS-inspired schema (timestamp, source.ip, event.category, event.action, etc.)
- SQLite backend for event storage and querying
- YAML correlation rule engine with field matching and time windows
- Alert generation and webhook dispatch
- CLI with `ingest`, `rules`, and `alerts` subcommands

## Skills developed

- ETL pipeline design (extract, transform, load)
- Event schema normalisation (ECS concepts)
- YAML-based rule authoring and evaluation
- SQL query building for time-windowed correlation
- Webhook integration for alert dispatch
- Plugin architecture for extensible ingestors

## How to run

```bash
cd mid/01-siem-lite
make install
python src/main.py ingest --source /var/log/auth.log --format syslog
python src/main.py rules --list
python src/main.py rules --run
python src/main.py alerts
```

## Stretch goals

- Add a real-time mode that tails log files and evaluates rules continuously
- Implement alert deduplication and suppression windows
- Add a basic web dashboard showing alert counts over time
- Support Elasticsearch as an alternative backend
- Add log enrichment (GeoIP, ASN, threat intel lookups) during ingestion
