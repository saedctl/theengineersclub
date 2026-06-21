"""Tests for Threat Feed Aggregator."""

import pytest
from src.main import sync_feeds, query_ioc


class TestSyncFeeds:
    # TODO: Test that syncing a mock feed stores IOCs in the database
    # TODO: Test that duplicate IOCs from different feeds are merged (sources combined)
    # TODO: Test that a feed connector failure doesn't crash the entire sync
    # TODO: Test that IOC confidence scores are updated on re-sync
    pass


class TestQueryIoc:
    # TODO: Test that querying an existing IP returns the correct IOC with all fields
    # TODO: Test that querying a non-existent value returns an empty result
    # TODO: Test that JSON output mode produces valid JSON
    # TODO: Test that an IOC with multiple sources lists all of them
    pass


class TestDeduplication:
    # TODO: Test that two IOCs with same value but different sources are merged into one
    # TODO: Test that merged IOC retains the highest confidence score
    # TODO: Test that tags from both sources are combined and deduplicated
    pass
