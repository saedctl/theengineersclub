"""Tests for Log Sentinel."""

import pytest
from src.main import parse_log_file, detect_brute_force, detect_sudo_abuse, filter_by_severity


class TestParseLogFile:
    # TODO: Test parsing a valid auth.log line extracts timestamp, source_ip, and event_type
    # TODO: Test parsing an nginx combined log line extracts IP, method, path, and status code
    # TODO: Test that an empty file returns an empty list
    # TODO: Test that malformed lines are skipped without crashing
    # TODO: Test that syslog format extracts hostname and process name
    pass


class TestDetectBruteForce:
    # TODO: Test that 5 failed logins from one IP in 30s triggers an alert
    # TODO: Test that 4 failed logins from one IP in 30s does NOT trigger (below threshold)
    # TODO: Test that 5 failed logins from one IP spread over 10 minutes does NOT trigger (outside window)
    # TODO: Test that two different IPs with 3 failures each do not trigger (per-IP counting)
    pass


class TestDetectSudoAbuse:
    # TODO: Test that a failed sudo attempt generates an alert
    # TODO: Test that sudo by an unexpected user generates an alert
    # TODO: Test that sudo by a user in the expected list does NOT generate an alert
    pass


class TestFilterBySeverity:
    # TODO: Test filtering with min_severity="high" excludes low and medium alerts
    # TODO: Test filtering with min_severity="low" includes all alerts
    # TODO: Test filtering an empty alert list returns an empty list
    pass
