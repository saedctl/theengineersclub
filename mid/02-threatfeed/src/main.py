"""Threat Feed Aggregator — Collect, deduplicate, and enrich IOCs from multiple feeds.

Suggested modules to build:
- feeds: Feed connector base class and implementations (otx, abuseipdb, urlhaus, feodo)
- models: Pydantic IOC schema (type, value, sources, confidence, tags, first_seen)
- dedup: Deduplication and merge logic across multiple sources
- enrichment: ASN/geo enrichment via ipinfo.io
- store: SQLite backend for IOC storage and querying
- api: FastAPI app for local IOC query endpoint
"""

import argparse
import sys


AVAILABLE_FEEDS = ["otx", "abuseipdb", "urlhaus", "feodo"]


def parse_args():
    parser = argparse.ArgumentParser(
        description="Aggregate threat intelligence feeds and query IOCs."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    sync_parser = subparsers.add_parser("sync", help="Sync IOCs from threat intelligence feeds")
    sync_parser.add_argument(
        "--feeds",
        default=",".join(AVAILABLE_FEEDS),
        help=f"Comma-separated list of feeds to sync ({','.join(AVAILABLE_FEEDS)})",
    )
    sync_parser.add_argument("--db", default="threatfeed.db", help="SQLite database path")

    query_parser = subparsers.add_parser("query", help="Query for an IOC by value")
    query_parser.add_argument("value", help="IOC value to look up (IP, domain, hash, URL)")
    query_parser.add_argument("--db", default="threatfeed.db", help="SQLite database path")
    query_parser.add_argument("--json", action="store_true", help="Output as JSON")

    return parser.parse_args()


def sync_feeds(feed_names: list[str], db_path: str):
    """Sync IOCs from the specified threat intelligence feeds."""
    # TODO: For each feed name, instantiate the appropriate feed connector
    # TODO: Fetch IOCs from each feed (handle errors per-feed, don't fail all on one error)
    # TODO: Normalise IOCs to the common schema
    # TODO: Deduplicate: if same IOC value exists, merge sources and update confidence
    # TODO: Enrich IPs with ASN and geo data from ipinfo.io
    # TODO: Store in SQLite
    # TODO: Print summary per feed (N new IOCs, M updated, K errors)
    raise NotImplementedError("Feed sync not implemented")


def query_ioc(value: str, db_path: str, as_json: bool = False):
    """Query the local IOC database for a specific value."""
    # TODO: Search SQLite for exact match on IOC value
    # TODO: Also search for partial matches (e.g., domain in URL)
    # TODO: Display results: type, value, sources, confidence, tags, first_seen, last_seen
    # TODO: If --json, output as JSON; otherwise, use rich table
    raise NotImplementedError("IOC query not implemented")


def main():
    args = parse_args()

    if args.command == "sync":
        feeds = [f.strip() for f in args.feeds.split(",")]
        invalid = [f for f in feeds if f not in AVAILABLE_FEEDS]
        if invalid:
            print(f"Unknown feeds: {', '.join(invalid)}")
            print(f"Available: {', '.join(AVAILABLE_FEEDS)}")
            sys.exit(1)
        # TODO: Call sync_feeds()
        print(f"Syncing feeds: {', '.join(feeds)}")
        print("Threat Feed is not yet implemented. Start building the feed connectors!")
        sys.exit(1)

    elif args.command == "query":
        # TODO: Call query_ioc()
        print(f"Querying for: {args.value}")
        print("Threat Feed is not yet implemented. Start building the query engine!")
        sys.exit(1)


if __name__ == "__main__":
    main()
