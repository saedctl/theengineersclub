"""EDR Collector — FastAPI app that receives and stores telemetry from EDR agents.

Suggested modules to build:
- api: FastAPI routes for receiving events and querying stored telemetry
- store: SQLite backend for telemetry storage
- models: Pydantic models for telemetry events
"""

# TODO: Create FastAPI app instance

# TODO: Define POST /api/events endpoint
#   - Accept telemetry event JSON
#   - Validate with pydantic model
#   - Store in SQLite database
#   - Return 201 Created

# TODO: Define GET /api/events endpoint
#   - Query parameters: agent_id, event_type, since, limit
#   - Return matching events from SQLite

# TODO: Define GET /api/agents endpoint
#   - List known agents with last_seen timestamp

# TODO: Define GET /api/health endpoint
#   - Return collector status and event count
