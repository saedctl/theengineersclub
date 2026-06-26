"""Tests for Hash Checker."""

import tempfile
import os
import pytest

from src.main import hash_file, verify_hash


class TestHashFile:
    # TODO: Test that hashing a file with known content returns the expected SHA-256 digest
    # TODO: Test that hashing the same file with algorithm="md5" returns the expected MD5 digest
    # TODO: Test that hashing a non-existent file raises FileNotFoundError

    def test_placeholder(self):
        pytest.skip("Implement hash_file tests")


class TestVerifyHash:
    # TODO: Test that verify_hash returns True when the expected hash matches
    # TODO: Test that verify_hash returns False when the expected hash does not match
    # TODO: Test that verification is case-insensitive (uppercase vs lowercase hex)

    def test_placeholder(self):
        pytest.skip("Implement verify_hash tests")
