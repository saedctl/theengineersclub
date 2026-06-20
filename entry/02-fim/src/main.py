"""File Integrity Monitor — Detect unauthorized filesystem changes.

Suggested modules to build:
- hasher: SHA-256 file hashing with streaming reads for large files
- walker: Directory tree traversal with exclude pattern support
- baseline: Baseline creation, storage (JSON), and loading
- differ: Compare current filesystem state against stored baseline
- reporter: Format and output change reports
"""

import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(
        description="Monitor file integrity by comparing filesystem state against a stored baseline."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    baseline_parser = subparsers.add_parser(
        "baseline", help="Create a new baseline snapshot of a directory"
    )
    baseline_parser.add_argument(
        "--path", required=True, help="Directory path to baseline"
    )
    baseline_parser.add_argument(
        "--output", default=".fim_baseline.json", help="Baseline output file path"
    )

    check_parser = subparsers.add_parser(
        "check", help="Check current state against stored baseline"
    )
    check_parser.add_argument(
        "--path", required=True, help="Directory path to check"
    )
    check_parser.add_argument(
        "--baseline", default=".fim_baseline.json", help="Baseline file to compare against"
    )

    return parser.parse_args()


def hash_file(filepath: str) -> str:
    """Compute SHA-256 hash of a file using streaming reads."""
    # TODO: Open file in binary mode, read in 8KB chunks
    # TODO: Feed each chunk to hashlib.sha256()
    # TODO: Return hex digest
    raise NotImplementedError("File hashing not implemented")


def walk_directory(path: str) -> list[dict]:
    """Walk a directory tree and collect file metadata.

    Returns a list of dicts with: filepath, sha256, size, mtime
    """
    # TODO: Use os.walk() to traverse the directory
    # TODO: For each file, compute hash and collect size + mtime
    # TODO: Store relative paths (relative to the base path)
    raise NotImplementedError("Directory walking not implemented")


def create_baseline(path: str, output: str):
    """Create a baseline snapshot and save to JSON."""
    # TODO: Walk the directory and collect file metadata
    # TODO: Serialize to JSON and write to output file
    # TODO: Print summary (number of files baselined)
    raise NotImplementedError("Baseline creation not implemented")


def check_against_baseline(path: str, baseline_file: str):
    """Compare current state against a stored baseline.

    Report:
    - New files (in current state but not in baseline)
    - Modified files (hash differs from baseline)
    - Deleted files (in baseline but not in current state)
    """
    # TODO: Load baseline from JSON file
    # TODO: Walk current directory state
    # TODO: Compare: find new, modified, and deleted files
    # TODO: Print report grouped by change type
    raise NotImplementedError("Baseline check not implemented")


def main():
    args = parse_args()

    if args.command == "baseline":
        # TODO: Validate path exists and is a directory
        # TODO: Call create_baseline()
        print(f"Creating baseline for {args.path}")
        print("FIM is not yet implemented. Start building the hasher and walker!")
        sys.exit(1)

    elif args.command == "check":
        # TODO: Validate path and baseline file exist
        # TODO: Call check_against_baseline()
        print(f"Checking {args.path} against baseline")
        print("FIM is not yet implemented. Start building the differ!")
        sys.exit(1)


if __name__ == "__main__":
    main()
