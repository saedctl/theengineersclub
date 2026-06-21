"""Tests for AI Threat Hunter."""

import pytest
from src.main import ingest_events, get_table_schema, nl_to_sql, check_api_key


class TestIngestEvents:
    # TODO: Test that ingesting a JSON file with 10 events creates 10 rows in DuckDB
    # TODO: Test that ingesting a CSV file correctly maps column headers to fields
    # TODO: Test that duplicate events (same ID) are handled (skip or update)
    # TODO: Test that ingesting an empty file creates the table but inserts 0 rows
    pass


class TestNlToSql:
    # TODO: Test that "show all events" translates to "SELECT * FROM events" (or similar)
    # TODO: Test that the generated SQL is a SELECT statement (not INSERT/UPDATE/DELETE)
    # TODO: Test that conversation history enables follow-up questions
    # TODO: Test that invalid questions return an appropriate error message
    pass


class TestGetTableSchema:
    # TODO: Test that schema output includes the events table with all expected columns
    # TODO: Test that schema is formatted as valid CREATE TABLE SQL
    pass


class TestCheckApiKey:
    # TODO: Test that missing ANTHROPIC_API_KEY causes sys.exit
    # TODO: Test that a set ANTHROPIC_API_KEY passes the check
    pass
