"""Tests for Port Scanner."""

import pytest
from src.main import parse_ports, fingerprint_service


class TestParsePorts:
    # TODO: Test that "80" returns [80]
    # TODO: Test that "1-5" returns [1, 2, 3, 4, 5]
    # TODO: Test that "22,80,443" returns [22, 80, 443]
    # TODO: Test that "22,80,100-102" returns [22, 80, 100, 101, 102]
    # TODO: Test that duplicate ports are deduplicated ("80,80" returns [80])
    # TODO: Test that ports outside 1-65535 raise ValueError
    # TODO: Test that invalid input like "abc" raises ValueError
    pass


class TestFingerprintService:
    # TODO: Test that a banner starting with "SSH-2.0" is identified as "ssh"
    # TODO: Test that a banner containing "HTTP/1.1" is identified as "http"
    # TODO: Test that port 443 with no banner is identified as "https"
    # TODO: Test that an unknown port with no banner returns "unknown"
    pass


class TestScanPort:
    # TODO: Test scanning localhost on a known-open port returns state="open"
    # TODO: Test scanning a known-closed port returns state="closed"
    # TODO: Test that timeout is respected (scan completes within 2x timeout)
    pass
