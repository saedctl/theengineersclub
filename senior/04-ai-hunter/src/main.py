"""AI Threat Hunter — LLM-assisted threat hunting with natural language queries.

Suggested modules to build:
- store: DuckDB event store — table creation, ingestion, and raw SQL execution
- llm: Claude API client for NL-to-SQL translation and event explanation
- ingest: Event ingestion pipeline (JSON, CSV) into DuckDB
- chat: Interactive chat loop with conversation context management
- models: Pydantic models for events and query results
"""

import argparse
import os
import sys


def parse_args():
    parser = argparse.ArgumentParser(
        description="LLM-assisted threat hunting — ask questions in English, get SQL results."
    )
    parser.add_argument("--db", default="events.duckdb", help="DuckDB database path")

    subparsers = parser.add_subparsers(dest="command", required=True)

    ingest_parser = subparsers.add_parser("ingest", help="Ingest security events into the store")
    ingest_parser.add_argument("--file", required=True, help="Path to event data file")
    ingest_parser.add_argument(
        "--format", choices=["json", "csv"], required=True, help="Input file format"
    )

    query_parser = subparsers.add_parser("query", help="Ask a natural language question")
    query_parser.add_argument("question", nargs="?", help="Question in plain English")

    explain_parser = subparsers.add_parser("explain", help="Get a detailed explanation of an event")
    explain_parser.add_argument("--event-id", required=True, help="Event ID to explain")

    subparsers.add_parser("chat", help="Start an interactive threat hunting chat session")

    return parser.parse_args()


def check_api_key():
    """Verify ANTHROPIC_API_KEY is set."""
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY environment variable is not set.")
        print("Get your API key from https://console.anthropic.com/")
        sys.exit(1)


def ingest_events(filepath: str, file_format: str, db_path: str):
    """Ingest security events from a file into DuckDB."""
    # TODO: Connect to DuckDB (create if not exists)
    # TODO: Create events table if not exists (id, timestamp, source_ip, dest_ip,
    #       event_type, severity, message, raw)
    # TODO: Parse input file (JSON array or CSV)
    # TODO: Insert events into DuckDB
    # TODO: Print summary (N events ingested)
    raise NotImplementedError("Event ingestion not implemented")


def get_table_schema(db_path: str) -> str:
    """Get the DuckDB table schema as a string for the LLM prompt."""
    # TODO: Query DuckDB for table definitions
    # TODO: Format as CREATE TABLE statements
    # TODO: Return schema string
    raise NotImplementedError("Schema retrieval not implemented")


def nl_to_sql(question: str, schema: str, conversation_history: list[dict] | None = None) -> str:
    """Translate a natural language question to SQL using Claude.

    The prompt should include:
    - The database schema
    - Instructions to return ONLY a SQL query
    - Conversation history for follow-up questions
    """
    # TODO: Build the system prompt with schema and instructions
    # TODO: Include conversation history for context
    # TODO: Call Claude API (claude-sonnet-4-6) with the question
    # TODO: Extract the SQL query from the response
    # TODO: Validate it's a SELECT query (prevent mutations)
    raise NotImplementedError("NL-to-SQL translation not implemented")


def explain_event(event_id: str, db_path: str):
    """Retrieve an event and ask Claude for a detailed security analysis."""
    # TODO: Query DuckDB for the event by ID
    # TODO: Build a prompt asking Claude to explain the event's security significance
    # TODO: Include context: what the event type means, potential risks, recommended actions
    # TODO: Display the explanation
    raise NotImplementedError("Event explanation not implemented")


def run_chat(db_path: str):
    """Run an interactive threat hunting chat loop."""
    # TODO: Get schema for the LLM prompt
    # TODO: Maintain conversation history
    # TODO: Loop: read user input, translate to SQL, execute, display results
    # TODO: Support special commands: "schema" (show tables), "quit" (exit), "clear" (reset history)
    raise NotImplementedError("Chat mode not implemented")


def main():
    args = parse_args()

    if args.command == "ingest":
        # TODO: Call ingest_events()
        print(f"Ingesting events from {args.file} ({args.format})")
        print("AI Threat Hunter is not yet implemented. Start building the DuckDB store!")
        sys.exit(1)

    elif args.command in ("query", "explain", "chat"):
        check_api_key()

        if args.command == "query":
            # TODO: Get schema, translate question to SQL, execute, display results
            print(f"Translating question to SQL: {args.question}")
            print("AI Threat Hunter is not yet implemented. Start building the LLM integration!")
            sys.exit(1)

        elif args.command == "explain":
            # TODO: Call explain_event()
            print(f"Explaining event: {args.event_id}")
            print("AI Threat Hunter is not yet implemented. Start building the explainer!")
            sys.exit(1)

        elif args.command == "chat":
            # TODO: Call run_chat()
            print("Starting interactive chat session...")
            print("AI Threat Hunter is not yet implemented. Start building the chat loop!")
            sys.exit(1)


if __name__ == "__main__":
    main()
