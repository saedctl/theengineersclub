"""Tests for Vulnerability Pipeline."""

import pytest
from src.main import deduplicate_findings, generate_report


class TestDeduplicateFindings:
    # TODO: Test that two findings with the same CVE ID from different scanners are merged into one
    # TODO: Test that the merged finding lists both scanner names
    # TODO: Test that the highest CVSS score is kept when merging
    # TODO: Test that findings with different CVE IDs are not merged
    # TODO: Test that findings with no CVE ID (e.g., misconfigurations) are kept separate
    pass


class TestRunScanner:
    # TODO: Test that a mock nmap XML output is correctly parsed into finding dicts
    # TODO: Test that a mock trivy JSON output is correctly parsed into finding dicts
    # TODO: Test that a scanner failure (non-zero exit code) is handled gracefully
    pass


class TestGenerateReport:
    # TODO: Test that markdown report contains a summary section with counts by severity
    # TODO: Test that HTML report is valid HTML with a findings table
    # TODO: Test that findings are sorted by severity (critical first)
    # TODO: Test that an empty findings list produces a report stating "no findings"
    pass
