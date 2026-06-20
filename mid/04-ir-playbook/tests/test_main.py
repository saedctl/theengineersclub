"""Tests for IR Playbook Engine."""

import pytest
from src.main import load_playbooks, match_playbook, execute_step, run_playbook


class TestLoadPlaybooks:
    # TODO: Test that loading from a directory with one YAML file returns one playbook
    # TODO: Test that a playbook without required fields (name, alert_type, steps) raises validation error
    # TODO: Test that an empty directory returns an empty list
    # TODO: Test that non-YAML files in the directory are ignored
    pass


class TestMatchPlaybook:
    # TODO: Test that alert type "brute_force" matches the brute_force_response playbook
    # TODO: Test that an unknown alert type returns None
    # TODO: Test that matching is exact (partial matches don't count)
    pass


class TestExecuteStep:
    # TODO: Test that dry_run=True logs the action but returns status="skipped"
    # TODO: Test that a block_ip step in live mode returns status="success" (with mock)
    # TODO: Test that an unknown action type raises an error or returns status="failed"
    # TODO: Test that step params are correctly interpolated with alert data
    pass


class TestRunPlaybook:
    # TODO: Test that all steps execute in order and results are collected
    # TODO: Test that on_failure="abort" stops execution when a step fails
    # TODO: Test that on_failure="continue" continues execution when a step fails
    pass
