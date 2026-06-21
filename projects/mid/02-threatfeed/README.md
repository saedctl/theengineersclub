# Threat Feed Aggregator

A threat intelligence aggregator that collects, deduplicates, and enriches indicators of compromise from multiple feeds.

## What it is

Threat Feed aggregates IOCs (indicators of compromise) from multiple public threat intelligence feeds — OTX, AbuseIPDB, URLhaus, and Feodo Tracker. It normalises them into a common schema, deduplicates across sources, enriches with ASN and geolocation data, stores everything in SQLite, and exposes a local FastAPI query endpoint.

Threat intelligence is the foundation of proactive security. SOC teams consume feeds to block known-bad IPs and domains, security engineers integrate them into detection pipelines, and analysts use them to understand threat actor infrastructure. Building an aggregator teaches you how feeds work, why normalisation matters, and how to build an API other tools can consume.

## What you'll build

- Feed connectors for OTX, AbuseIPDB, URLhaus, and Feodo Tracker
- Common IOC schema (type, value, sources, confidence, tags, first_seen, last_seen)
- Deduplication logic merging IOCs from multiple sources
- ASN and geolocation enrichment via ipinfo.io
- SQLite storage with full-text search
- FastAPI local query API for IOC lookups
- CLI with `sync` and `query` subcommands

## Skills developed

- Threat intelligence feed integration and parsing
- Data normalisation and deduplication across heterogeneous sources
- IOC data modelling and confidence scoring
- REST API design with FastAPI
- Async HTTP requests for parallel feed fetching

## How to run

```bash
cd projects/mid/02-threatfeed
make install
python src/main.py sync --feeds otx,urlhaus,feodo
python src/main.py query 1.2.3.4
python src/main.py query evil-domain.com
# Start the local API server:
uvicorn src.api:app --reload
```

## Stretch goals

- Add STIX/TAXII feed support
- Implement IOC aging and automatic expiration
- Add a confidence decay model (older IOCs get lower confidence)
- Export IOCs in STIX 2.1 format
- Build a feed health dashboard tracking freshness and error rates
