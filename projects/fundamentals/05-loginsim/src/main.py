#!/usr/bin/env python3
"""Login Simulator — mock authentication with hashing, lockout, and session tracking."""

import argparse
import getpass
import json
import os
import sys
from datetime import datetime, timezone

import bcrypt


USER_DB_PATH = "users.json"
MAX_FAILED_ATTEMPTS = 5


def load_users(db_path: str = USER_DB_PATH) -> dict:
    """Load the user database from a JSON file.

    TODO:
        - If the file exists, read and parse it as JSON
        - If the file doesn't exist, return an empty dict
        - Handle JSON decode errors gracefully
    """
    raise NotImplementedError("Implement load_users")


def save_users(users: dict, db_path: str = USER_DB_PATH) -> None:
    """Save the user database to a JSON file.

    TODO:
        - Write the users dict to the file as formatted JSON
    """
    raise NotImplementedError("Implement save_users")


def hash_password(password: str) -> str:
    """Hash a password using bcrypt.

    Args:
        password: Plain-text password.

    Returns:
        Bcrypt hash as a string.

    TODO:
        - Use bcrypt.gensalt() to generate a salt
        - Use bcrypt.hashpw() to hash the password
        - Return the hash as a UTF-8 string
    """
    raise NotImplementedError("Implement hash_password")


def verify_password(password: str, hashed: str) -> bool:
    """Verify a password against a bcrypt hash.

    Args:
        password: Plain-text password to check.
        hashed: Stored bcrypt hash.

    Returns:
        True if the password matches the hash.

    TODO:
        - Use bcrypt.checkpw() to compare the password against the hash
        - Return True if they match, False otherwise
    """
    raise NotImplementedError("Implement verify_password")


def register_user(username: str, password: str, db_path: str = USER_DB_PATH) -> bool:
    """Register a new user.

    Args:
        username: Desired username.
        password: Plain-text password.
        db_path: Path to the user database file.

    Returns:
        True if registration succeeded, False if username already exists.

    TODO:
        - Load existing users
        - Check if username already exists (return False if so)
        - Hash the password
        - Store user record: password_hash, failed_attempts=0, locked=False, login_history=[]
        - Save users and return True
    """
    raise NotImplementedError("Implement register_user")


def login_user(username: str, password: str, db_path: str = USER_DB_PATH) -> dict:
    """Attempt to log in a user.

    Args:
        username: Username to authenticate.
        password: Plain-text password.
        db_path: Path to the user database file.

    Returns:
        Dict with keys: success (bool), message (str).

    TODO:
        - Load users and check if username exists
        - Check if account is locked (return failure if so)
        - Verify the password against the stored hash
        - On success: reset failed_attempts to 0, log the attempt, return success
        - On failure: increment failed_attempts, log the attempt
        - If failed_attempts >= MAX_FAILED_ATTEMPTS: set locked=True
        - Save users and return the result
    """
    raise NotImplementedError("Implement login_user")


def get_user_status(username: str, db_path: str = USER_DB_PATH) -> dict | None:
    """Get the status of a user account.

    Args:
        username: Username to look up.
        db_path: Path to the user database file.

    Returns:
        Dict with account info, or None if user doesn't exist.

    TODO:
        - Load users and look up the username
        - Return a dict with: username, locked, failed_attempts, login_history
        - Return None if user doesn't exist
    """
    raise NotImplementedError("Implement get_user_status")


def cmd_register(args: argparse.Namespace) -> None:
    """Handle the 'register' subcommand.

    TODO:
        - Prompt for a password using getpass.getpass (hides input)
        - Call register_user with the username and password
        - Print success or failure message
    """
    raise NotImplementedError("Implement cmd_register")


def cmd_login(args: argparse.Namespace) -> None:
    """Handle the 'login' subcommand.

    TODO:
        - Prompt for a password using getpass.getpass
        - Call login_user with the username and password
        - Print the result message
        - Exit with code 0 on success, 1 on failure
    """
    raise NotImplementedError("Implement cmd_login")


def cmd_status(args: argparse.Namespace) -> None:
    """Handle the 'status' subcommand.

    TODO:
        - Call get_user_status with the username
        - Print account info: locked status, failed attempts, recent login history
        - Print 'user not found' if None is returned
    """
    raise NotImplementedError("Implement cmd_status")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="loginsim",
        description="Mock authentication system with hashing and lockout.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    register_parser = subparsers.add_parser("register", help="Register a new user")
    register_parser.add_argument("username", help="Username to register")
    register_parser.set_defaults(func=cmd_register)

    login_parser = subparsers.add_parser("login", help="Log in as a user")
    login_parser.add_argument("username", help="Username to log in as")
    login_parser.set_defaults(func=cmd_login)

    status_parser = subparsers.add_parser("status", help="Show account status")
    status_parser.add_argument("username", help="Username to check")
    status_parser.set_defaults(func=cmd_status)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
