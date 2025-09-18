# ITMO-InfoSec-HW2

## Задание

### 1. Разработайте docker-compose для стенда

Контейнеры:
- attacker: образ kali-linux (kalilinux/kali-rolling:latest)
- victim: образ alpine:latest

Обе машины в одной docker-сети. Откройте shell в обеих для тестирования трафика. Не забудьте установить нужные утилиты (ping, curl и пр.) внутри kali/alpine, а так же запустить простой http-сервер на жертве. ICMP на victim должен быть блокирован Suricata (пакеты не проходят).

### 2. Проверьте работу Suricata
От имени attacker проверьте:
- ping victim
- curl http://victim
- tail -f /var/log/suricata/eve.json | jq '.'
- В логе Suricata (`eve.json`) должны появиться события drop для ICMP и
отдельные записи для HTTP-запросов.
- В victim пакеты ICMP не должны проходить (нет ответа на ping).

3. Задание со звездочкой - запустите suricata в единой сети docker в режиме IDS. Рассмотрите вопрос, какие ограничения существуют на запуск Suricata в режиме IPS в среде docker.
