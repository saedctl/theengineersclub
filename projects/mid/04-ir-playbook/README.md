# IR Playbook Engine

A YAML-driven incident response playbook engine that automates containment, investigation, and notification steps.

## What it is

IR Playbook Engine loads incident response playbooks from YAML files, matches them to alert types, and executes response steps in sequence. Steps include actions like blocking IPs, revoking tokens, collecting logs, sending notifications, and creating tickets. All actions are logged to an immutable audit trail. A `--dry-run` mode lets you validate playbooks without executing real actions.

Incident response under pressure is where playbooks save careers. Manually running through a 15-step containment procedure at 3 AM is error-prone. Automating it — with guardrails, dry-run capability, and full audit logging — is what senior IR engineers and DevSecOps teams build. This project teaches you to think about IR as code.

## What you'll build

- YAML playbook loader and validator
- Alert-to-playbook matching engine
- Step executors: block_ip, revoke_token, collect_logs, notify, create_ticket
- Dry-run mode that logs what would happen without executing
- Immutable audit log of all actions taken
- CLI with `trigger`, `playbooks`, and `audit` subcommands

## Skills developed

- YAML schema design for operational workflows
- Command pattern for pluggable step execution
- Audit logging and non-repudiation
- Dry-run / simulation architecture
- Error handling in multi-step automated workflows

## How to run

```bash
cd projects/mid/04-ir-playbook
make install
python src/main.py playbooks --list
python src/main.py trigger --alert brute_force --data '{"source_ip": "1.2.3.4"}' --dry-run
python src/main.py trigger --alert brute_force --data '{"source_ip": "1.2.3.4"}'
python src/main.py audit --last 20
```

## Stretch goals

- Add parallel step execution for independent actions
- Implement step rollback on failure (undo block, restore token)
- Add approval gates — pause and wait for human approval before critical steps
- Integrate with PagerDuty or Slack for real notifications
- Build a playbook testing framework that simulates alerts and validates outcomes
