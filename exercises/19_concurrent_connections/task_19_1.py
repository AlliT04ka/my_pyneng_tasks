# -*- coding: utf-8 -*-
"""
Задание 19.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции ping_ip_addresses:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.

Подсказка о работе с concurrent.futures:
Если необходимо пинговать несколько IP-адресов в разных потоках,
надо создать функцию, которая будет пинговать один IP-адрес,
а затем запустить эту функцию в разных потоках для разных
IP-адресов с помощью concurrent.futures (это надо сделать в функции ping_ip_addresses).
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
import subprocess
import time


def ping_ip(ip_address):
    reply = subprocess.run(['ping', '-c', '3', '-n', ip_address])
    if reply.returncode == 0:
        return {ip_address: True}
    else:
        return {ip_address: False}


def ping_ip_addresses(ip_list, limit=3):
    data = {}
    alive = []
    unreachable = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        future_ping = [executor.submit(ping_ip, ip) for ip in ip_list]
        for f in as_completed(future_ping):
            data.update(f.result())
        for ip in ip_list:
            if data[ip]:
                alive.append(ip)
            else:
                unreachable.append(ip)
    return alive, unreachable
