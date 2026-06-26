#!/usr/bin/env python3
"""Hash Checker — compute and verify cryptographic hashes of files."""

import argparse
import hashlib
import sys


def hash_file(path: str, algorithm: str = "sha256") -> str:
    """Compute the cryptographic hash of a file.

    Args:
        path: Path to the file to hash.
        algorithm: Hash algorithm to use (md5, sha256).

    Returns:
        Hex digest string of the file's hash.

    TODO:
        - Open the file in binary read mode
        - Read the file in chunks (e.g. 8192 bytes) to handle large files
        - Feed each chunk into a hashlib hash object
        - Return the hex digest
    """
    raise NotImplementedError("Implement hash_file")


def verify_hash(path: str, expected: str, algorithm: str = "sha256") -> bool:
    """Verify a file's hash against an expected value.

    Args:
        path: Path to the file to verify.
        expected: Expected hex digest string.
        algorithm: Hash algorithm to use (md5, sha256).

    Returns:
        True if the computed hash matches the expected value.

    TODO:
        - Call hash_file to compute the actual hash
        - Compare it against the expected value (case-insensitive)
        - Return True if they match, False otherwise
    """
    raise NotImplementedError("Implement verify_hash")


def cmd_hash(args: argparse.Namespace) -> None:
    """Handle the 'hash' subcommand.

    TODO:
        - Call hash_file with args.file and args.algorithm
        - Print the algorithm, file path, and resulting hash
        - Handle FileNotFoundError gracefully
    """
    raise NotImplementedError("Implement cmd_hash")


def cmd_verify(args: argparse.Namespace) -> None:
    """Handle the 'verify' subcommand.

    TODO:
        - Call verify_hash with args.file, args.expected, and args.algorithm
        - Print whether the hash matches or not
        - Exit with code 0 on match, 1 on mismatch
        - Handle FileNotFoundError gracefully
    """
    raise NotImplementedError("Implement cmd_verify")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="hashcheck",
        description="Compute and verify cryptographic hashes of files.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    hash_parser = subparsers.add_parser("hash", help="Compute a file's hash")
    hash_parser.add_argument("file", help="Path to the file to hash")
    hash_parser.add_argument(
        "--algorithm", "-a", default="sha256", choices=["md5", "sha256"],
        help="Hash algorithm (default: sha256)",
    )
    hash_parser.set_defaults(func=cmd_hash)

    verify_parser = subparsers.add_parser("verify", help="Verify a file against an expected hash")
    verify_parser.add_argument("file", help="Path to the file to verify")
    verify_parser.add_argument("expected", help="Expected hex digest")
    verify_parser.add_argument(
        "--algorithm", "-a", default="sha256", choices=["md5", "sha256"],
        help="Hash algorithm (default: sha256)",
    )
    verify_parser.set_defaults(func=cmd_verify)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
