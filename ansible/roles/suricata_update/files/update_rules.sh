#!/usr/bin/env bash

set -euo pipefail

CURRENT_DIR="$(dirname "$(readlink -f "$0")")"
CURRENT_FILE="$(readlink -f "$0")"
LOG_FILE_PATH="${1:-/var/log/suricata/update_rules.log}"

echo "[$(date -Iseconds)] === Starting Suricata rules update ===" | tee -a $LOG_FILE_PATH

echo "[$(date -Iseconds)] [1/3] Fetch + merge rules via suricata-update..." | tee -a $LOG_FILE_PATH
if !suricata-update >> "$LOG_FILE_PATH" 2>&1; then
    echo "[$(date -Iseconds)] ERROR: suricata-update failed, aborting." | tee -a "$LOG_FILE_PATH"
    exit 1
fi

echo "[$(date -Iseconds)] [2/3] Test Suricata configuration..." | tee -a "$LOG_FILE_PATH"
if !suricata -T -c /etc/suricata/suricata.yaml >> "$LOG_FILE_PATH" 2>&1; then
    echo "[$(date -Iseconds)] ERROR: suricata -T failed, NOT reloading service." | tee -a "$LOG_FILE_PATH"
    exit 1
fi

echo "[$(date -Iseconds)] [3/3] Reload Suricata service..." | tee -a "$LOG_FILE_PATH"
if systemctl reload suricata 2>>"$LOG_FILE_PATH"; then
    echo "[$(date -Iseconds)] SUCCESS: Rules updated and Suricata reloaded." | tee -a "$LOG_FILE_PATH"
else
    echo "[$(date -Iseconds)] WARNING: reload failed, trying restart..." | tee -a "$LOG_FILE_PATH"
    systemctl restart suricata
fi