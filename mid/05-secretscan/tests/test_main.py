"""Tests for Secret Scanner."""

import pytest
from src.main import scan_line, calculate_entropy, scan_file, SECRET_PATTERNS


class TestScanLine:
    # TODO: Test that "AKIAIOSFODNN7EXAMPLE" is detected as aws_access_key
    # TODO: Test that "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" is detected as github_classic_token
    # TODO: Test that a string matching the Stripe secret key pattern is detected as stripe_secret_key
    # TODO: Test that a normal code line with no secrets returns an empty list
    # TODO: Test that matched text is redacted in the finding (not exposing the full secret)
    pass


class TestCalculateEntropy:
    # TODO: Test that "aaaaaaa" has entropy close to 0.0
    # TODO: Test that a random 40-char hex string has entropy above 3.5
    # TODO: Test that "password123" has lower entropy than "kX9$mQ2v!zR4pL8w"
    pass


class TestScanFile:
    # TODO: Test that scanning a file with an AWS key on line 5 reports the finding with correct line number
    # TODO: Test that scanning a binary file does not crash
    # TODO: Test that scanning an empty file returns an empty list
    # TODO: Test that high-entropy strings above the threshold are flagged
    pass


class TestSecretPatterns:
    # TODO: Test each regex pattern in SECRET_PATTERNS matches its expected format
    # TODO: Test that patterns don't match overly broad strings (false positive check)
    pass
