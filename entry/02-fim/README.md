# File Integrity Monitor (FIM)

A file integrity monitoring tool that detects unauthorized changes to files and directories.

## What it is

FIM walks a directory tree, computes SHA-256 hashes for every file, and stores the results as a JSON baseline. On subsequent runs, it compares the current state against the baseline and reports new, modified, and deleted files.

File integrity monitoring is a foundational security control required by PCI-DSS, HIPAA, and most compliance frameworks. Tools like OSSEC, AIDE, and Tripwire do this at enterprise scale. Building one from scratch teaches you how hashing, filesystem traversal, and change detection actually work under the hood.

## What you'll build

- Directory tree walker that computes SHA-256 hashes for all files
- JSON baseline storage (filepath, hash, size, last modified)
- Diff engine comparing current state vs stored baseline
- Detection of new files, modified files, and deleted files
- `baseline` subcommand to create/update the baseline
- `check` subcommand to compare against baseline and report changes

## Skills developed

- Cryptographic hashing (SHA-256) for integrity verification
- Filesystem traversal and metadata collection
- JSON serialization for state persistence
- Diffing algorithms and change detection
- CLI design with subcommands

## How to run

```bash
cd entry/02-fim
make install
python src/main.py baseline --path /etc/nginx
python src/main.py check --path /etc/nginx
```

## Stretch goals

- Add `--exclude` patterns (e.g., skip `.git/`, `*.pyc`, `node_modules/`)
- Implement `--watch` mode using filesystem events (watchdog)
- Add file permission change detection (mode, owner, group)
- Support multiple baseline profiles (dev, staging, prod)
- Generate a summary report with severity ratings (config files changed = high)
