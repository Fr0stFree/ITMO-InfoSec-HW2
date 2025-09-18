[Unit]
Description=Suricata Intrusion Detection Service
After=network.target

[Service]
PIDFile=/run/suricata.pid
Type=forking
Restart=on-failure
ExecStart=
ExecStart=/usr/bin/suricata -c /etc/suricata/suricata.yaml -q 1 --pidfile /run/suricata.pid

[Install]
WantedBy=multi-user.target
