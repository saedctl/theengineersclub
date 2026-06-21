# Adversary Simulator

A MITRE ATT&CK-mapped adversary simulation framework for testing detection capabilities in isolated lab environments.

> **WARNING: This tool simulates real attack techniques. It must ONLY be run in isolated lab environments that you own and control. Never run against production systems, shared networks, or systems you do not have explicit authorisation to test. Misuse may violate computer fraud laws.**

## What it is

Adversary Simulator executes MITRE ATT&CK techniques in a controlled environment to test whether your detection stack catches them. It includes TTP modules for command execution (T1059), valid accounts (T1078), brute force (T1110), credential dumping (T1003), and C2 communication (T1071). A YAML scenario runner chains techniques into multi-stage attack simulations, and a coverage reporter compares simulated TTPs against your detection rules.

Purple teaming — the practice of simulating attacks and validating detections — is how mature security teams find gaps. Tools like Atomic Red Team, MITRE Caldera, and Cobalt Strike do this commercially. Building a simulation framework teaches you how attack techniques actually work, how to design safe execution boundaries, and how to measure detection coverage.

## What you'll build

- TTP modules mapped to MITRE ATT&CK techniques (T1059, T1078, T1110, T1003, T1071)
- YAML scenario runner for multi-stage attack chains
- Coverage reporter comparing simulated TTPs against detection rules
- Safe execution boundaries with pre/post validation
- CLI with `list`, `run`, `scenario`, and `coverage` subcommands

## Skills developed

- MITRE ATT&CK framework understanding
- Attack technique simulation (safe implementations)
- Multi-stage attack chain design
- Detection coverage gap analysis
- Safety engineering (guardrails, sandboxing, confirmation prompts)

## How to run

```bash
cd projects/senior/03-advsim
make install
python src/main.py list
python src/main.py run --technique T1059 --target localhost
python src/main.py scenario --file src/scenarios/initial_access.yaml
python src/main.py coverage --rules-dir ../01-detect-engine/src/rules/
```

## Stretch goals

- Add technique cleanup/rollback after execution
- Implement a telemetry listener to confirm which techniques generated detectable events
- Add a report card comparing expected detections vs actual detections
- Build a web UI for scenario authoring and execution monitoring
- Add support for multi-host scenarios (simulate lateral movement)
