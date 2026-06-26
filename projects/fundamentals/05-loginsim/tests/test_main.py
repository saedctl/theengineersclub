"""Tests for Login Simulator."""

import os
import tempfile
import pytest

from src.main import (
    hash_password,
    verify_password,
    register_user,
    login_user,
    get_user_status,
)


class TestPasswordHashing:
    # TODO: Test that hash_password returns a valid bcrypt hash (starts with '$2b$')
    # TODO: Test that hashing the same password twice produces different hashes (salting)
    # TODO: Test that verify_password returns True for a correct password

    def test_placeholder(self):
        pytest.skip("Implement password hashing tests")


class TestRegistration:
    # TODO: Test that registering a new user returns True and the user exists in the DB
    # TODO: Test that registering a duplicate username returns False
    # TODO: Test that the stored password is hashed, not plain text

    def test_placeholder(self):
        pytest.skip("Implement registration tests")


class TestLogin:
    # TODO: Test that login with correct credentials returns success=True
    # TODO: Test that login with wrong password returns success=False
    # TODO: Test that 5 consecutive failed logins locks the account
    # TODO: Test that a locked account rejects even correct credentials

    def test_placeholder(self):
        pytest.skip("Implement login tests")


class TestUserStatus:
    # TODO: Test that get_user_status returns None for a non-existent user
    # TODO: Test that status shows correct failed_attempts count after failed logins
    # TODO: Test that status shows locked=True after account lockout

    def test_placeholder(self):
        pytest.skip("Implement user status tests")
