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
