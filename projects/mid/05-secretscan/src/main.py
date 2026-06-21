"""Secret Scanner — Detect leaked secrets in git repos and filesystems.

Suggested modules to build:
- patterns: Regex pattern library for known secret types
- entropy: Shannon entropy calculator for high-entropy string detection
- scanner: File and directory scanning engine
- git_scanner: GitPython-based commit history scanner
- hook: Pre-commit hook installer
- models: Finding model with file, line, pattern_name, matched_text (redacted), confidence
"""

import argparse
import sys


SECRET_PATTERNS = {
    "aws_access_key": r"AKIA[0-9A-Z]{16}",
    "aws_secret_key": r"(?i)aws_secret_access_key\s*[=:]\s*[A-Za-z0-9/+=]{40}",
    "github_token": r"gh[pousr]_[A-Za-z0-9_]{36,255}",
    "github_classic_token": r"ghp_[A-Za-z0-9]{36}",
    "stripe_secret_key": r"sk_live_[A-Za-z0-9]{24,99}",
    "stripe_publishable_key": r"pk_live_[A-Za-z0-9]{24,99}",
    "rsa_private_key": r"-----BEGIN RSA PRIVATE KEY-----",
    "ec_private_key": r"-----BEGIN EC PRIVATE KEY-----",
    "generic_private_key": r"-----BEGIN PRIVATE KEY-----",
    "jwt": r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}",
    "connection_string": r"(?i)(mongodb|postgres|mysql|redis):\/\/[^\s\"']+@[^\s\"']+",
}


def parse_args():
    parser = argparse.ArgumentParser(
        description="Scan for leaked secrets in source code and git history."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    repo_parser = subparsers.add_parser("repo", help="Scan a git repository for secrets")
    repo_parser.add_argument("--path", required=True, help="Path to the git repository")
    repo_parser.add_argument(
        "--history", action="store_true", help="Scan full git commit history, not just working tree"
    )
    repo_parser.add_argument(
        "--entropy-threshold", type=float, default=4.5,
        help="Minimum Shannon entropy to flag a string (default: 4.5)",
    )

    file_parser = subparsers.add_parser("file", help="Scan a single file for secrets")
    file_parser.add_argument("--path", required=True, help="Path to the file to scan")

    hook_parser = subparsers.add_parser("install-hook", help="Install as a pre-commit hook")
    hook_parser.add_argument("--repo", required=True, help="Path to the git repository")

    return parser.parse_args()


def scan_line(line: str, line_number: int, filepath: str) -> list[dict]:
    """Scan a single line for secret patterns."""
    # TODO: Test each regex pattern against the line
    # TODO: For each match, create a finding dict with: filepath, line_number, pattern_name,
    #       matched_text (redacted — show first 4 and last 4 chars only), confidence
    raise NotImplementedError("Line scanning not implemented")


def calculate_entropy(text: str) -> float:
    """Calculate Shannon entropy of a string."""
    # TODO: Count character frequencies
    # TODO: Calculate entropy using -sum(p * log2(p))
    raise NotImplementedError("Entropy calculation not implemented")


def scan_file(filepath: str, entropy_threshold: float = 4.5) -> list[dict]:
    """Scan a file for secrets using pattern matching and entropy analysis."""
    # TODO: Read file line by line
    # TODO: Apply pattern matching via scan_line()
    # TODO: For each line, also check for high-entropy strings (split by whitespace, quotes, etc.)
    # TODO: Return combined list of findings
    raise NotImplementedError("File scanning not implemented")


def scan_repo(repo_path: str, scan_history: bool, entropy_threshold: float) -> list[dict]:
    """Scan a git repository for secrets."""
    # TODO: If scan_history is False, just walk the working tree and scan each file
    # TODO: If scan_history is True, use GitPython to iterate all commits
    # TODO: For each commit, check the diff for added lines containing secrets
    # TODO: Return findings with commit hash and author info when scanning history
    raise NotImplementedError("Repository scanning not implemented")


def install_pre_commit_hook(repo_path: str):
    """Install a pre-commit hook that runs the secret scanner."""
    # TODO: Write a shell script to .git/hooks/pre-commit
    # TODO: The script should run this scanner on staged files
    # TODO: Exit with non-zero status if secrets are found (blocking the commit)
    # TODO: Make the hook executable
    raise NotImplementedError("Hook installation not implemented")


def main():
    args = parse_args()

    if args.command == "repo":
        # TODO: Validate repo path is a git repository
        # TODO: Call scan_repo()
        # TODO: Display findings with rich formatting
        mode = "full history" if args.history else "working tree"
        print(f"Scanning repository at {args.path} ({mode})")
        print("Secret Scanner is not yet implemented. Start building the pattern matcher!")
        sys.exit(1)

    elif args.command == "file":
        # TODO: Validate file exists
        # TODO: Call scan_file()
        # TODO: Display findings
        print(f"Scanning file: {args.path}")
        print("Secret Scanner is not yet implemented. Start building the file scanner!")
        sys.exit(1)

    elif args.command == "install-hook":
        # TODO: Call install_pre_commit_hook()
        print(f"Installing pre-commit hook in {args.repo}")
        print("Secret Scanner is not yet implemented. Start building the hook installer!")
        sys.exit(1)


if __name__ == "__main__":
    main()
