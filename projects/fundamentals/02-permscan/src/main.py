#!/usr/bin/env python3
"""Permission Scanner — find files with overly permissive access rights."""

import argparse
import os
import stat
import sys


def get_permission_string(mode: int) -> str:
    """Convert a file mode to a human-readable permission string (e.g. rwxr-xr--).

    Args:
        mode: File mode from os.stat().

    Returns:
        Permission string like 'rwxr-xr--'.

    TODO:
        - Extract the user/group/other read, write, execute bits from mode
        - Build a 9-character string (e.g. 'rwxr-xr--')
        - Return the string
    """
    raise NotImplementedError("Implement get_permission_string")


def is_world_readable(mode: int) -> bool:
    """Check if a file is world-readable.

    TODO:
        - Use stat.S_IROTH to check the other-read bit
        - Return True if set
    """
    raise NotImplementedError("Implement is_world_readable")


def is_world_writable(mode: int) -> bool:
    """Check if a file is world-writable.

    TODO:
        - Use stat.S_IWOTH to check the other-write bit
        - Return True if set
    """
    raise NotImplementedError("Implement is_world_writable")


def is_suid(mode: int) -> bool:
    """Check if a file has the SUID bit set.

    TODO:
        - Use stat.S_ISUID to check the set-user-ID bit
        - Return True if set
    """
    raise NotImplementedError("Implement is_suid")


def is_sgid(mode: int) -> bool:
    """Check if a file has the SGID bit set.

    TODO:
        - Use stat.S_ISGID to check the set-group-ID bit
        - Return True if set
    """
    raise NotImplementedError("Implement is_sgid")


def scan_directory(path: str, filter_type: str | None = None) -> list[dict]:
    """Walk a directory tree and find files with permission issues.

    Args:
        path: Root directory to scan.
        filter_type: Optional filter — 'world-readable', 'world-writable', 'suid', 'sgid'.

    Returns:
        List of dicts with keys: path, permissions, issues.

    TODO:
        - Use os.walk to traverse the directory tree
        - For each file, call os.stat to get the file mode
        - Check for world-readable, world-writable, SUID, and SGID issues
        - If filter_type is set, only include files matching that filter
        - Return a list of findings (each as a dict)
    """
    raise NotImplementedError("Implement scan_directory")


def cmd_scan(args: argparse.Namespace) -> None:
    """Handle the 'scan' subcommand.

    TODO:
        - Call scan_directory with args.path and args.filter
        - Print results as a formatted table (path, permissions, issues)
        - If no issues found, print a reassuring message
        - Handle PermissionError for unreadable directories
    """
    raise NotImplementedError("Implement cmd_scan")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="permscan",
        description="Scan directories for overly permissive file access rights.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    scan_parser = subparsers.add_parser("scan", help="Scan a directory for permission issues")
    scan_parser.add_argument("path", help="Directory to scan")
    scan_parser.add_argument(
        "--filter", "-f",
        choices=["world-readable", "world-writable", "suid", "sgid"],
        help="Only show files matching this issue type",
    )
    scan_parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="Show all files, not just those with issues",
    )
    scan_parser.set_defaults(func=cmd_scan)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
