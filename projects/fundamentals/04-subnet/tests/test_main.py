"""Tests for Subnet Calculator."""

import pytest

from src.main import parse_network, get_network_info, check_contains


class TestParseNetwork:
    # TODO: Test that '192.168.1.0/24' is parsed without error
    # TODO: Test that '192.168.1.100/24' with host bits set is accepted (strict=False)
    # TODO: Test that an invalid string like 'not-a-network' raises ValueError

    def test_placeholder(self):
        pytest.skip("Implement parse_network tests")


class TestGetNetworkInfo:
    # TODO: Test that 192.168.1.0/24 returns network_address='192.168.1.0', broadcast='192.168.1.255', num_hosts=254
    # TODO: Test that 10.0.0.0/8 returns the correct first_host='10.0.0.1' and last_host='10.255.255.254'
    # TODO: Test that a /32 returns num_hosts=1 (single host)

    def test_placeholder(self):
        pytest.skip("Implement get_network_info tests")


class TestCheckContains:
    # TODO: Test that 192.168.1.50 is in 192.168.1.0/24
    # TODO: Test that 192.168.2.1 is NOT in 192.168.1.0/24
    # TODO: Test that the network address itself is reported as contained

    def test_placeholder(self):
        pytest.skip("Implement check_contains tests")
