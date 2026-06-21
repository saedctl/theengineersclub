"""Tests for Detection Engine."""

import pytest
from src.main import parse_sigma_rule, compile_to_sql, compile_to_elasticsearch, compile_to_splunk, validate_rules


class TestParseSigmaRule:
    # TODO: Test that parsing the ssh_brute_force rule extracts title, level, and logsource
    # TODO: Test that the detection section is parsed into selection criteria
    # TODO: Test that the condition string is correctly interpreted
    # TODO: Test that a rule missing required fields raises a validation error
    # TODO: Test that tags are preserved in the parsed model
    pass


class TestCompileToSql:
    # TODO: Test that a simple field=value selection compiles to "WHERE field = 'value'"
    # TODO: Test that a wildcard value compiles to "WHERE field LIKE '%value%'"
    # TODO: Test that multiple selections with AND compile to "WHERE a = 'x' AND b = 'y'"
    # TODO: Test that a count condition compiles to GROUP BY with HAVING
    pass


class TestCompileToElasticsearch:
    # TODO: Test that a simple selection compiles to a bool/must/term query
    # TODO: Test that OR conditions compile to bool/should queries
    # TODO: Test that the output is valid JSON-serializable dict
    pass


class TestCompileToSplunk:
    # TODO: Test that a simple selection compiles to 'index=* EventType="value"'
    # TODO: Test that logsource fields map to index and sourcetype
    # TODO: Test that count conditions compile to "| stats count by SourceIP | where count > 5"
    pass


class TestValidateRules:
    # TODO: Test that a valid rule passes validation
    # TODO: Test that a rule missing 'detection' key fails validation
    # TODO: Test that a rule with invalid condition syntax fails validation
    pass
