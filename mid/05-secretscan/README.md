# Secret Scanner

A tool for detecting leaked secrets in git repositories and filesystems using regex patterns and entropy analysis.

## What it is

Secret Scanner detects hardcoded secrets — AWS keys, GitHub tokens, Stripe keys, private keys, JWTs, and database connection strings — in source code and git history. It combines regex-based pattern matching for known secret formats with Shannon entropy analysis for detecting high-entropy strings that may be secrets. It can scan the current filesystem, walk full git commit history, and install as a pre-commit hook to prevent future leaks.

Secrets in source code are one of the most common and damaging security issues in software engineering. Tools like TruffleHog, Gitleaks, and detect-secrets address this at scale. Building your own teaches you the detection techniques, the false positive challenges, and why pre-commit prevention beats post-hoc scanning.

## What you'll build

- Regex pattern library for AWS keys, GitHub tokens, Stripe keys, RSA/EC private keys, JWTs, connection strings
- Shannon entropy scanner for high-entropy string detection
- Filesystem scanner (walk files, apply patterns)
- Git history scanner using GitPython (scan all commits, not just HEAD)
- Pre-commit hook installer
- CLI with `repo`, `file`, and `install-hook` subcommands

## Skills developed

- Regex engineering for security-sensitive pattern matching
- Information entropy analysis
- Git internals (walking commit history, diffs, blobs)
- Pre-commit hook architecture
- False positive management and tuning

## How to run

```bash
cd mid/05-secretscan
make install
python src/main.py repo --path /path/to/repo
python src/main.py repo --path /path/to/repo --history
python src/main.py file --path /path/to/config.py
python src/main.py install-hook --repo /path/to/repo
```

## Stretch goals

- Add a `--baseline` mode to mark known false positives and exclude them from future scans
- Implement `--fix` mode that replaces detected secrets with environment variable references
- Add Slack/webhook notification for CI pipeline integration
- Support custom regex rules via a YAML config file
- Add a `--sarif` output format for GitHub Advanced Security integration
