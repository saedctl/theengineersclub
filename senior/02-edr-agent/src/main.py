"""EDR Agent — Host-based endpoint detection and response.

Suggested modules to build:
- process_monitor: Track process creation and command lines using psutil
- network_monitor: Track network connections (new outbound, unusual ports)
- file_monitor: Watch sensitive paths for changes using watchdog
- telemetry: HTTP client that streams events to the collector
- yara_engine: Load and match YARA rules against observed events
- daemon: Background execution and PID file management
"""

import argparse
import sys


SENSITIVE_PATHS = [
    "/etc/passwd",
    "/etc/shadow",
    "/etc/sudoers",
    "/etc/ssh/sshd_config",
    "/etc/crontab",
    "/var/spool/cron",
    "/root/.ssh/authorized_keys",
    "/home/*/.ssh/authorized_keys",
    "/etc/ld.so.preload",
    "/etc/systemd/system",
    "/tmp",
    "/var/tmp",
]


def parse_args():
    parser = argparse.ArgumentParser(
        description="Host-based EDR agent — monitor processes, network, and file events."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    start_parser = subparsers.add_parser("start", help="Start the EDR agent")
    start_parser.add_argument(
        "--collector",
        default="http://localhost:9000",
        help="Collector endpoint URL (default: http://localhost:9000)",
    )
    start_parser.add_argument(
        "--foreground", action="store_true", help="Run in foreground instead of daemonising"
    )
    start_parser.add_argument(
        "--yara-rules", default="rules/", help="Directory containing YARA rules"
    )
    start_parser.add_argument(
        "--pid-file", default="/tmp/edr-agent.pid", help="PID file path"
    )

    subparsers.add_parser("stop", help="Stop the running EDR agent")
    subparsers.add_parser("status", help="Check if the agent is running")

    return parser.parse_args()


def monitor_processes(callback):
    """Monitor new process creation using psutil.

    For each new process, collect: pid, name, cmdline, username, create_time, parent_pid
    """
    # TODO: Snapshot current process list
    # TODO: Poll periodically for new processes (diff against snapshot)
    # TODO: For each new process, extract metadata and call callback(event)
    # TODO: Flag suspicious patterns: reverse shells, encoded commands, LOLBins
    raise NotImplementedError("Process monitoring not implemented")


def monitor_network(callback):
    """Monitor network connections using psutil.

    Track new outbound connections, connections to unusual ports, and high-volume activity.
    """
    # TODO: Get current connections via psutil.net_connections()
    # TODO: Track new connections that weren't in the previous snapshot
    # TODO: Collect: pid, local_addr, remote_addr, status, associated process name
    # TODO: Flag suspicious patterns: connections to known-bad ports, C2 beacons
    raise NotImplementedError("Network monitoring not implemented")


def monitor_files(paths: list[str], callback):
    """Monitor file events on sensitive paths using watchdog.

    Watch for: created, modified, deleted, moved events.
    """
    # TODO: Set up watchdog observers for each sensitive path
    # TODO: For each event, collect: event_type, path, timestamp
    # TODO: Call callback(event) for each observed change
    raise NotImplementedError("File monitoring not implemented")


def stream_telemetry(event: dict, collector_url: str):
    """Send a telemetry event to the collector via HTTP POST."""
    # TODO: Serialize event as JSON
    # TODO: POST to collector_url/api/events
    # TODO: Handle connection errors gracefully (buffer and retry)
    raise NotImplementedError("Telemetry streaming not implemented")


def match_yara_rules(event: dict, rules_dir: str) -> list[dict]:
    """Match YARA rules against event data."""
    # TODO: Load compiled YARA rules from directory
    # TODO: Match against event data (command lines, file contents)
    # TODO: Return list of matches with rule name and metadata
    raise NotImplementedError("YARA matching not implemented")


def main():
    args = parse_args()

    if args.command == "start":
        # TODO: Check if agent is already running (PID file)
        # TODO: If not foreground, daemonise
        # TODO: Start all monitors with telemetry callback
        # TODO: Run event loop
        print(f"Starting EDR agent (collector: {args.collector})")
        print("EDR Agent is not yet implemented. Start building the process monitor!")
        sys.exit(1)

    elif args.command == "stop":
        # TODO: Read PID file
        # TODO: Send SIGTERM to the agent process
        print("Stopping EDR agent...")
        print("EDR Agent is not yet implemented.")
        sys.exit(1)

    elif args.command == "status":
        # TODO: Check if PID file exists and process is running
        print("Checking EDR agent status...")
        print("EDR Agent is not yet implemented.")
        sys.exit(1)


if __name__ == "__main__":
    main()
