"""IR Playbook Engine — YAML-driven incident response automation.

Suggested modules to build:
- loader: YAML playbook loader and validator
- matcher: Alert-type to playbook matching engine
- executor: Step executor with action implementations (block_ip, revoke_token, etc.)
- audit: Immutable audit log writer and reader
- models: Pydantic models for playbooks, steps, alerts, and audit entries
"""

import argparse
import json
import sys


def parse_args():
    parser = argparse.ArgumentParser(
        description="Execute incident response playbooks triggered by security alerts."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    trigger_parser = subparsers.add_parser("trigger", help="Trigger a playbook for an alert")
    trigger_parser.add_argument("--alert", required=True, help="Alert type (e.g., brute_force)")
    trigger_parser.add_argument("--data", required=True, help="Alert data as JSON string")
    trigger_parser.add_argument(
        "--dry-run", action="store_true", help="Simulate execution without taking real actions"
    )
    trigger_parser.add_argument(
        "--playbooks-dir", default="src/playbooks", help="Directory containing playbook YAML files"
    )

    playbooks_parser = subparsers.add_parser("playbooks", help="List available playbooks")
    playbooks_parser.add_argument(
        "--list", action="store_true", required=True, help="List all playbooks"
    )
    playbooks_parser.add_argument(
        "--playbooks-dir", default="src/playbooks", help="Directory containing playbook YAML files"
    )

    audit_parser = subparsers.add_parser("audit", help="View the audit log")
    audit_parser.add_argument("--last", type=int, default=20, help="Number of recent entries to show")
    audit_parser.add_argument("--audit-file", default="audit.log", help="Path to audit log file")

    return parser.parse_args()


def load_playbooks(playbooks_dir: str) -> list[dict]:
    """Load and validate all YAML playbooks from a directory."""
    # TODO: Scan directory for .yaml files
    # TODO: Parse each file and validate required fields (name, alert_type, steps)
    # TODO: Validate each step has: action, params
    # TODO: Return list of playbook dicts
    raise NotImplementedError("Playbook loading not implemented")


def match_playbook(alert_type: str, playbooks: list[dict]) -> dict | None:
    """Find the playbook that matches the given alert type."""
    # TODO: Search playbooks for matching alert_type
    # TODO: Return the matching playbook or None
    raise NotImplementedError("Playbook matching not implemented")


def execute_step(step: dict, alert_data: dict, dry_run: bool) -> dict:
    """Execute a single playbook step.

    Supported actions: block_ip, revoke_token, collect_logs, notify, create_ticket
    """
    # TODO: Dispatch to the appropriate action handler based on step["action"]
    # TODO: If dry_run, log what would happen but don't execute
    # TODO: Return result dict with: action, status (success/skipped/failed), details
    raise NotImplementedError("Step execution not implemented")


def run_playbook(playbook: dict, alert_data: dict, dry_run: bool) -> list[dict]:
    """Execute all steps in a playbook sequentially."""
    # TODO: Iterate through playbook steps
    # TODO: Execute each step, collecting results
    # TODO: If a step fails, decide whether to continue or abort (based on step config)
    # TODO: Write all results to audit log
    # TODO: Return list of step results
    raise NotImplementedError("Playbook execution not implemented")


def write_audit_entry(entry: dict, audit_file: str):
    """Append an entry to the immutable audit log."""
    # TODO: Add timestamp to entry
    # TODO: Append as JSON line to audit file
    raise NotImplementedError("Audit logging not implemented")


def main():
    args = parse_args()

    if args.command == "trigger":
        try:
            alert_data = json.loads(args.data)
        except json.JSONDecodeError:
            print("Error: --data must be valid JSON")
            sys.exit(1)
        # TODO: Load playbooks from directory
        # TODO: Match alert type to playbook
        # TODO: Execute matched playbook (with dry_run flag)
        mode = "DRY RUN" if args.dry_run else "LIVE"
        print(f"[{mode}] Triggering playbook for alert: {args.alert}")
        print("IR Playbook Engine is not yet implemented. Start building the loader and executor!")
        sys.exit(1)

    elif args.command == "playbooks":
        # TODO: Load and list all playbooks
        print("Listing playbooks...")
        print("IR Playbook Engine is not yet implemented. Start building the loader!")
        sys.exit(1)

    elif args.command == "audit":
        # TODO: Read and display recent audit log entries
        print(f"Showing last {args.last} audit entries...")
        print("IR Playbook Engine is not yet implemented. Start building the audit log!")
        sys.exit(1)


if __name__ == "__main__":
    main()
