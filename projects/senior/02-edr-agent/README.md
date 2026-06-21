# EDR Agent

A host-based endpoint detection and response agent that monitors process creation, network connections, and file events.

## What it is

EDR Agent monitors a host for suspicious activity by watching process creation via psutil, tracking network connections, and observing file events on sensitive paths using watchdog. Telemetry is streamed to a collector via HTTP, and local YARA rules are evaluated against observed events. The collector is a separate FastAPI app that receives and stores telemetry.

EDR is the backbone of modern endpoint security. Products like CrowdFalcon, SentinelOne, and Microsoft Defender for Endpoint run agents on every host in an enterprise. Building a minimal EDR agent teaches you how telemetry collection works, what data sources matter, and how detection logic runs at the endpoint level rather than in a central SIEM.

## What you'll build

- Process monitor using psutil (new processes, suspicious command lines)
- Network connection tracker (new outbound connections, unusual ports)
- File event watcher on sensitive paths using watchdog
- Telemetry streamer to a collector endpoint via HTTP
- Local YARA rule matching against observed events
- Collector app (FastAPI) that receives and stores telemetry
- CLI with `start`, `stop`, and `status` subcommands

## Skills developed

- System telemetry collection (processes, network, filesystem)
- Event-driven architecture with watchdog
- HTTP streaming for real-time data delivery
- YARA rule authoring and matching
- Daemon/service design patterns
- Client-server architecture

## How to run

```bash
cd projects/senior/02-edr-agent
make install

# Start the collector (in one terminal):
uvicorn src.collector:app --port 9000

# Start the agent (in another terminal):
python src/main.py start --collector http://localhost:9000 --foreground
python src/main.py status
python src/main.py stop
```

## Stretch goals

- Add process tree tracking (parent-child relationships)
- Implement DNS query monitoring
- Add registry key monitoring (Windows) or plist monitoring (macOS)
- Build a web dashboard for the collector showing live telemetry
- Implement threat scoring based on combined signals (process + network + file)
