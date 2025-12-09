.PHONY: all fetch generate test deploy status clean

all: fetch generate test deploy status

fetch:
	@echo "[*] Stage 1/4: Fetching external feeds..."
	@./fetch_feeds.sh

generate:
	@echo "[*] Stage 2/4: Generating custom_ioc.rules..."
	@sudo python3 generate_custom_ioc_rules.py

test:
	@echo "[*] Stage 3/4: Testing Suricata configuration..."
	@sudo suricata -T -c /etc/suricata/suricata.yaml

deploy:
	@echo "[*] Stage 4/4: Deploying rules (reload Suricata)..."
	@sudo systemctl reload suricata || sudo systemctl restart suricata
	@echo "[+] Pipeline completed successfully!"

status:
	@echo "[*] Checking Suricata status..."
	@sudo systemctl status suricata --no-pager | head -10

clean:
	@echo "[*] Cleaning feeds directory..."
	@rm -rf feeds/
