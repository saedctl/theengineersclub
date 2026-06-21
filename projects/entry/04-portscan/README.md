# Port Scanner

A multi-threaded TCP connect scanner with banner grabbing and service fingerprinting.

## What it is

A TCP connect scanner that uses Python's `socket` library and `ThreadPoolExecutor` for concurrent scanning. It identifies open ports, grabs service banners, and attempts basic service fingerprinting. Results are displayed as a rich terminal table.

Port scanning is the starting point for almost every penetration test and network assessment. Understanding how TCP connections work, what banner grabbing reveals, and how services identify themselves gives you foundational knowledge that applies to both offensive and defensive security work.

## What you'll build

- TCP connect scanner using socket library
- Multi-threaded scanning with ThreadPoolExecutor
- Port range parser supporting ranges (1-1024) and comma-separated lists (22,80,443)
- Banner grabbing (read first bytes from open ports)
- Basic service fingerprinting (match banners to known services)
- Rich terminal output with colour-coded results

## Skills developed

- TCP/IP networking fundamentals (three-way handshake, connect scan)
- Concurrent programming with ThreadPoolExecutor
- Socket programming and timeout handling
- Service identification and banner analysis
- Input parsing for flexible port specifications

## How to run

```bash
cd projects/entry/04-portscan
make install
python src/main.py 192.168.1.1 --ports 1-1024 --threads 50
python src/main.py scanme.nmap.org --ports 22,80,443,8080
python src/main.py 10.0.0.1 --ports 1-65535 --threads 100
```

**Note:** Only scan hosts you own or have explicit permission to scan.

## Stretch goals

- Add UDP scanning support
- Implement SYN scanning (requires raw sockets / root)
- Add OS fingerprinting based on TCP/IP stack behaviour
- Export results in Nmap XML format for tool interoperability
- Add `--rate` flag to limit packets per second
