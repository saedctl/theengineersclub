"""Tests for Password Auditor."""

import pytest
from src.main import calculate_entropy, detect_patterns, check_wordlist, check_hibp


class TestCalculateEntropy:
    # TODO: Test that "aaaa" has lower entropy than "aB3$xZ9!"
    # TODO: Test that an empty string returns 0.0 entropy
    # TODO: Test that a single repeated character (e.g., "aaaaaaa") has 0.0 entropy
    # TODO: Test that entropy increases with character set diversity
    pass


class TestDetectPatterns:
    # TODO: Test that "qwerty" is detected as a keyboard walk
    # TODO: Test that "01012024" is detected as a date pattern
    # TODO: Test that "p@ssw0rd" is detected as l33t speak
    # TODO: Test that "aaa111" is detected as repeated characters
    # TODO: Test that a random string like "kX9$mQ2v" returns no patterns
    pass


class TestCheckWordlist:
    # TODO: Test that "password" is found in the wordlist
    # TODO: Test that "Password1" (common variation) is flagged
    # TODO: Test that a random 20-char string is NOT found in the wordlist
    pass


class TestCheckHibp:
    # TODO: Test that "password" returns a count > 0 (it has been breached millions of times)
    # TODO: Test that the function correctly parses the HIBP API response format
    # TODO: Test that network errors are handled gracefully
    pass
