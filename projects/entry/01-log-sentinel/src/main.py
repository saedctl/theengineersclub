"""Log Sentinel — Log analysis and alerting for security operations.

Suggested modules to build:
- parsers: Format-specific log parsers (auth, syslog, nginx)
- detectors: Pattern detection engines (brute_force, sudo_abuse, anomaly)
- threshold: Sliding window threshold engine (count events in time window)
- alerts: Alert model and JSON output formatter
- filters: Severity filtering and alert deduplication
"""

import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(
        description="Parse security logs and detect suspicious patterns."
    )
    parser.add_argument(
        "--file",
        required=True,
        help="Path to log file to analyse",
    )
    parser.add_argument(
        "--format",
        choices=["auth", "syslog", "nginx"],
        required=True,
        help="Log format to parse",
    )
    parser.add_argument(
        "--severity",
        choices=["low", "medium", "high", "critical"],
        default="low",
        help="Minimum severity level to report (default: low)",
    )
    return parser.parse_args()


def parse_log_file(filepath: str, log_format: str) -> list[dict]:
    """Parse a log file into structured event dicts.

    Each event dict should contain at minimum:
    - timestamp (datetime)
    - source_ip (str, if applicable)
    - message (str)
    - event_type (str)
    """
    # TODO: Implement format-specific parsers
    # - auth format: parse /var/log/auth.log lines (sshd, sudo, etc.)
    # - syslog format: parse standard syslog lines (timestamp, host, process, message)
    # - nginx format: parse combined access log (ip, timestamp, method, path, status, ua)
    raise NotImplementedError(f"Parser for '{log_format}' format not implemented")


def detect_brute_force(events: list[dict], threshold: int = 5, window_seconds: int = 60) -> list[dict]:
    """Detect brute-force login attempts.

    Look for N or more failed authentication events from the same source IP
    within a sliding time window of T seconds.
    """
    # TODO: Group events by source IP
    # TODO: Implement sliding window — for each IP, check if count >= threshold within window
    # TODO: Return alert dicts with: source_ip, event_count, window_start, window_end, severity
    raise NotImplementedError("Brute-force detection not implemented")


def detect_sudo_abuse(events: list[dict]) -> list[dict]:
    """Detect suspicious sudo usage.

    Flag sudo commands from users not in an expected-sudoers list,
    or sudo failures (authentication failure).
    """
    # TODO: Filter events for sudo-related messages
    # TODO: Check for failed sudo attempts
    # TODO: Check for sudo usage by unexpected users
    # TODO: Return alert dicts with: user, command, timestamp, severity
    raise NotImplementedError("Sudo abuse detection not implemented")


def filter_by_severity(alerts: list[dict], min_severity: str) -> list[dict]:
    """Filter alerts to only include those at or above min_severity."""
    severity_order = {"low": 0, "medium": 1, "high": 2, "critical": 3}
    # TODO: Filter alerts where alert severity >= min_severity
    raise NotImplementedError("Severity filtering not implemented")


def format_alerts_json(alerts: list[dict]) -> str:
    """Format alerts as JSON output."""
    # TODO: Serialize alerts to JSON with proper datetime handling
    raise NotImplementedError("JSON alert formatting not implemented")


def main():
    args = parse_args()

    # TODO: Validate that the log file exists and is readable
    # TODO: Parse the log file using the appropriate format parser
    # TODO: Run all detectors (brute_force, sudo_abuse) against parsed events
    # TODO: Filter alerts by minimum severity
    # TODO: Output alerts as JSON to stdout

    print(f"Analysing {args.file} as {args.format} format (min severity: {args.severity})")
    print("Log Sentinel is not yet implemented. Start building the parsers and detectors!")
    sys.exit(1)


if __name__ == "__main__":
    main()
