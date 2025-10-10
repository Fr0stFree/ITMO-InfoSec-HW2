# Help

### Проверить iptables:
```bash
sudo iptables -L DOCKER-USER -nv --line-numbers
```

### Проверить Логи:
```bash
journalctl -u suricata.service -b
sudo tail -n 200 /var/log/suricata/suricata.log
sudo tail -n 0 -f /var/log/suricata/fast.log
sudo tail -n 0 -f /var/log/suricata/eve.json | jq .
```

### Запустить suricata вручную:
```bash
sudo suricata -c /etc/suricata/suricata.yaml -q 0
```

### NMAP scans:
```bash
nmap -sS victim     # SYN scan
nmap -sX victim     # Xmas scan
nmap -sU victim     # UDP scan
nmap -O victim      # OS detection
```