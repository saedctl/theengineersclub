"""SIEM Lite — Lightweight log ingestion, correlation, and alerting.

Suggested modules to build:
- ingestors: Pluggable log parsers (syslog, json, csv) that emit normalised events
- schema: ECS-inspired event model (pydantic) with fields like timestamp, source.ip, event.category
- store: SQLite backend for event storage and querying
- rules: YAML rule loader and correlation engine with time-window support
- alerts: Alert model and webhook dispatcher
- cli: Click-based CLI with ingest/rules/alerts commands
"""

import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(
        description="Lightweight SIEM — ingest logs, correlate events, generate alerts."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    ingest_parser = subparsers.add_parser("ingest", help="Ingest log data into the event store")
    ingest_parser.add_argument("--source", required=True, help="Path to log file or directory")
    ingest_parser.add_argument(
        "--format",
        choices=["syslog", "json", "csv"],
        required=True,
        help="Log format to parse",
    )
    ingest_parser.add_argument("--db", default="siem.db", help="SQLite database path")

    rules_parser = subparsers.add_parser("rules", help="Manage and run correlation rules")
    rules_group = rules_parser.add_mutually_exclusive_group(required=True)
    rules_group.add_argument("--list", action="store_true", help="List all available rules")
    rules_group.add_argument("--run", action="store_true", help="Run all rules against stored events")
    rules_parser.add_argument("--rules-dir", default="src/rules", help="Directory containing YAML rules")
    rules_parser.add_argument("--db", default="siem.db", help="SQLite database path")

    alerts_parser = subparsers.add_parser("alerts", help="View generated alerts")
    alerts_parser.add_argument("--db", default="siem.db", help="SQLite database path")
    alerts_parser.add_argument("--last", type=int, default=50, help="Number of recent alerts to show")
    alerts_parser.add_argument("--severity", choices=["low", "medium", "high", "critical"],
                               help="Filter by minimum severity")

    return parser.parse_args()


def ingest_logs(source: str, log_format: str, db_path: str):
    """Ingest logs from a source file, normalise, and store in SQLite."""
    # TODO: Select the appropriate ingestor based on format
    # TODO: Parse each log line into a normalised event dict (ECS-inspired schema)
    # TODO: Insert normalised events into SQLite events table
    # TODO: Print summary (N events ingested from source)
    raise NotImplementedError("Log ingestion not implemented")


def list_rules(rules_dir: str):
    """List all YAML correlation rules in the rules directory."""
    # TODO: Scan rules_dir for .yaml files
    # TODO: Parse each rule and display: name, description, severity, time_window
    raise NotImplementedError("Rule listing not implemented")


def run_rules(rules_dir: str, db_path: str):
    """Run all correlation rules against stored events."""
    # TODO: Load all rules from rules_dir
    # TODO: For each rule, query SQLite for matching events within the rule's time window
    # TODO: If match count >= rule threshold, generate an alert
    # TODO: Store alerts in SQLite alerts table
    # TODO: Optionally dispatch alerts to webhook
    raise NotImplementedError("Rule execution not implemented")


def show_alerts(db_path: str, last: int, severity: str | None):
    """Display recent alerts from the alert store."""
    # TODO: Query SQLite for recent alerts
    # TODO: Filter by severity if specified
    # TODO: Display as rich table
    raise NotImplementedError("Alert display not implemented")


def main():
    args = parse_args()

    if args.command == "ingest":
        # TODO: Validate source file exists
        # TODO: Call ingest_logs()
        print(f"Ingesting {args.source} as {args.format}")
        print("SIEM Lite is not yet implemented. Start building the ingestors!")
        sys.exit(1)

    elif args.command == "rules":
        if args.list:
            # TODO: Call list_rules()
            print("Listing rules...")
        else:
            # TODO: Call run_rules()
            print("Running rules...")
        print("SIEM Lite is not yet implemented. Start building the rule engine!")
        sys.exit(1)

    elif args.command == "alerts":
        # TODO: Call show_alerts()
        print("Showing alerts...")
        print("SIEM Lite is not yet implemented. Start building the alert store!")
        sys.exit(1)


if __name__ == "__main__":
    main()
