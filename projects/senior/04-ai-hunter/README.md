# AI Threat Hunter

An LLM-assisted threat hunting tool that translates natural language queries to SQL and explains security events.

## What it is

AI Threat Hunter combines a DuckDB event store with Claude API integration to enable natural language threat hunting. Ingest security events from JSON or CSV, then ask questions in plain English — the tool translates them to SQL via Claude, executes the query, and returns results. An explain mode provides detailed analysis of specific events, and an interactive chat loop maintains conversation context for iterative investigation.

The intersection of AI and security operations is where the industry is heading. Analysts spend hours writing queries to hunt for threats. LLM-assisted hunting lets analysts describe what they're looking for in natural language and get immediate results. Building this teaches you how to integrate LLMs into security workflows, manage prompt engineering for structured output, and design tools that augment human analysts.

## What you'll build

- DuckDB event store for fast analytical queries over security logs
- Claude API integration for natural language to SQL translation
- Event ingestion pipeline (JSON, CSV formats)
- Natural language query interface
- Event explanation mode (detailed analysis of a specific event)
- Interactive chat loop with conversation context

## Skills developed

- LLM API integration (Claude) with structured output
- Prompt engineering for SQL generation
- Analytical database design (DuckDB)
- Interactive CLI design with conversation state
- Security event analysis and threat hunting methodology

## How to run

```bash
cd projects/senior/04-ai-hunter
make install
export ANTHROPIC_API_KEY=your-key-here
python src/main.py ingest --file events.json --format json
python src/main.py query "Show me all failed SSH logins in the last 24 hours"
python src/main.py explain --event-id evt-12345
python src/main.py chat
```

**Requires:** An Anthropic API key set as `ANTHROPIC_API_KEY` environment variable.

## Stretch goals

- Add follow-up question support ("now filter those to just external IPs")
- Implement query caching so repeated questions don't consume API tokens
- Add a `--validate` flag that shows the generated SQL before executing
- Support multiple event stores (switching between different DuckDB databases)
- Build an anomaly detection prompt that identifies statistical outliers in event data
