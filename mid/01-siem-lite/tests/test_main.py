"""Tests for SIEM Lite."""

import pytest
from src.main import ingest_logs, run_rules, show_alerts


class TestIngestLogs:
    # TODO: Test that ingesting a syslog file creates normalised events with timestamp and source.ip
    # TODO: Test that ingesting a JSON log file parses each line as a JSON object
    # TODO: Test that ingesting a CSV file uses the header row as field names
    # TODO: Test that malformed lines are skipped and logged rather than crashing
    # TODO: Test that duplicate events (same timestamp + source + message) are deduplicated
    pass


class TestRuleEngine:
    # TODO: Test that a brute-force rule triggers when 5+ failed logins from one IP appear in 120s
    # TODO: Test that the rule does NOT trigger when events are spread across different IPs
    # TODO: Test that the rule does NOT trigger when event count is below threshold
    # TODO: Test that the time_window is correctly enforced (events outside window are excluded)
    pass


class TestAlerts:
    # TODO: Test that generated alerts contain rule_name, severity, matched_events count, and timestamp
    # TODO: Test that severity filtering works (--severity high excludes medium/low)
    # TODO: Test that --last N returns at most N alerts
    pass
