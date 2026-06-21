"""Tests for File Integrity Monitor."""

import pytest
from src.main import hash_file, walk_directory, check_against_baseline


class TestHashFile:
    # TODO: Test that hashing a known file produces the expected SHA-256 digest
    # TODO: Test that hashing the same file twice returns the same digest
    # TODO: Test that hashing two different files returns different digests
    # TODO: Test that hashing a non-existent file raises FileNotFoundError
    pass


class TestWalkDirectory:
    # TODO: Test that walking a directory with 3 files returns 3 entries
    # TODO: Test that each entry contains filepath, sha256, size, and mtime keys
    # TODO: Test that filepaths are stored as relative paths
    # TODO: Test that walking an empty directory returns an empty list
    # TODO: Test that subdirectories are traversed recursively
    pass


class TestCheckAgainstBaseline:
    # TODO: Test that a new file (not in baseline) is reported as added
    # TODO: Test that a modified file (different hash) is reported as modified
    # TODO: Test that a missing file (in baseline but deleted) is reported as deleted
    # TODO: Test that an unchanged directory reports no changes
    pass
