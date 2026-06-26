#!/usr/bin/env python3
"""Subnet Calculator — calculate network details from CIDR notation."""

import argparse
import ipaddress
import sys


def parse_network(cidr: str) -> ipaddress.IPv4Network:
    """Parse a CIDR string into an IPv4Network object.

    Args:
        cidr: Network in CIDR notation (e.g. '192.168.1.0/24').

    Returns:
        An IPv4Network object.

    TODO:
        - Use ipaddress.IPv4Network to parse the CIDR string
        - Use strict=False to allow host bits to be set
        - Handle ValueError for invalid input
    """
    raise NotImplementedError("Implement parse_network")


def get_network_info(cidr: str) -> dict:
    """Calculate all network details for a CIDR notation string.

    Args:
        cidr: Network in CIDR notation.

    Returns:
        Dict with keys: network_address, broadcast_address, subnet_mask,
        wildcard_mask, first_host, last_host, num_hosts, prefix_length.

    TODO:
        - Call parse_network to get the IPv4Network object
        - Extract network_address, broadcast_address, netmask (subnet_mask)
        - Calculate the wildcard mask (inverse of subnet mask)
        - Determine first and last usable host addresses
        - Count total usable hosts (num_addresses - 2 for /31+, handle /32 and /31 edge cases)
        - Return all values as a dict
    """
    raise NotImplementedError("Implement get_network_info")


def check_contains(cidr: str, ip: str) -> bool:
    """Check if an IP address falls within a subnet.

    Args:
        cidr: Network in CIDR notation.
        ip: IP address to check.

    Returns:
        True if the IP is in the subnet.

    TODO:
        - Parse the network with parse_network
        - Parse the IP with ipaddress.IPv4Address
        - Use the 'in' operator to check membership
    """
    raise NotImplementedError("Implement check_contains")


def cmd_info(args: argparse.Namespace) -> None:
    """Handle the 'info' subcommand.

    TODO:
        - Call get_network_info with args.cidr
        - Print each field in a clear, labelled format
        - Handle invalid CIDR input gracefully
    """
    raise NotImplementedError("Implement cmd_info")


def cmd_contains(args: argparse.Namespace) -> None:
    """Handle the 'contains' subcommand.

    TODO:
        - Call check_contains with args.cidr and args.ip
        - Print whether the IP is in the subnet or not
        - Exit with code 0 if contained, 1 if not
    """
    raise NotImplementedError("Implement cmd_contains")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="subnet",
        description="Calculate network details from CIDR notation.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    info_parser = subparsers.add_parser("info", help="Show network details for a CIDR range")
    info_parser.add_argument("cidr", help="Network in CIDR notation (e.g. 192.168.1.0/24)")
    info_parser.set_defaults(func=cmd_info)

    contains_parser = subparsers.add_parser("contains", help="Check if an IP is in a subnet")
    contains_parser.add_argument("cidr", help="Network in CIDR notation")
    contains_parser.add_argument("ip", help="IP address to check")
    contains_parser.set_defaults(func=cmd_contains)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
