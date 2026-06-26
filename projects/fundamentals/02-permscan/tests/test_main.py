"""Tests for Permission Scanner."""

import os
import stat
import tempfile
import pytest

from src.main import (
    get_permission_string,
    is_world_readable,
    is_world_writable,
    is_suid,
    is_sgid,
    scan_directory,
)


class TestPermissionString:
    # TODO: Test that mode 0o755 returns 'rwxr-xr-x'
    # TODO: Test that mode 0o644 returns 'rw-r--r--'
    # TODO: Test that mode 0o777 returns 'rwxrwxrwx'

    def test_placeholder(self):
        pytest.skip("Implement get_permission_string tests")


class TestPermissionChecks:
    # TODO: Test that is_world_readable returns True for mode 0o644 and False for 0o640
    # TODO: Test that is_world_writable returns True for mode 0o666 and False for 0o644
    # TODO: Test that is_suid returns True for mode 0o4755 and False for 0o755

    def test_placeholder(self):
        pytest.skip("Implement permission check tests")


class TestScanDirectory:
    # TODO: Test scanning a temp directory with a world-writable file flags it
    # TODO: Test scanning with filter='world-writable' excludes world-readable-only files
    # TODO: Test scanning an empty directory returns no findings

    def test_placeholder(self):
        pytest.skip("Implement scan_directory tests")
