#!/usr/bin/env bash
set -euo pipefail

FEEDS_DIR="$(dirname "$0")/feeds"

mkdir -p "$FEEDS_DIR"

echo "[1/4] Downloading Feodo Tracker IP blocklist..."
curl -sS "https://feodotracker.abuse.ch/downloads/ipblocklist.txt" \
    -o "${FEEDS_DIR}/feodo_ips.txt"

echo "[2/4] Downloading URLhaus IP blocklist..."
curl -sS "https://urlhaus.abuse.ch/downloads/text_recent/" \
    -o "${FEEDS_DIR}/urlhaus_ips.txt"

echo "[3/4] Downloading Botvrij.eu Destination IPs..."
curl -sS "https://www.botvrij.eu/data/ioclist.ip-dst.raw" \
    -o "${FEEDS_DIR}/botvrij_ips.txt"

echo "[4/4] Done. Feeds saved to: ${FEEDS_DIR}"
