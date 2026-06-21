"""Tests for GRC Audit."""

import pytest
from src.main import collect_config, load_controls, evaluate_control, generate_report


class TestCollectConfig:
    # TODO: Test that mock collector returns a dict with expected resource types (iam, s3, cloudtrail)
    # TODO: Test that mock IAM config includes root_account with access_keys and mfa fields
    # TODO: Test that unknown target type raises an error
    pass


class TestLoadControls:
    # TODO: Test that loading cis-aws controls from the controls directory returns the 3 starter controls
    # TODO: Test that each control has required fields: id, title, severity, check_type, check_params
    # TODO: Test that loading a non-existent framework returns an empty list
    pass


class TestEvaluateControl:
    # TODO: Test that CIS-AWS-1.4 passes when root has no active access keys
    # TODO: Test that CIS-AWS-1.4 fails when root has active access keys
    # TODO: Test that evaluation result contains control_id, status, and evidence
    # TODO: Test that a control with missing config data returns status="error"
    pass


class TestGenerateReport:
    # TODO: Test that markdown report contains a summary table with pass/fail counts
    # TODO: Test that HTML report is valid HTML with framework name in the title
    # TODO: Test that failed controls include remediation recommendations
    pass
