# -*- coding: utf-8 -*-
"""
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.

Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример итогового списка:
["Loopback0", "Tunnel0", "Ethernet0/1", "Ethernet0/3.100", "Ethernet1/0"]

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
"""
import re


def get_ints_without_description(file_name):
    all_interfaces = []
    intrf_with_desc = dict()
    with open(file_name, 'r') as f:
        for line in f:
            match_intrf = re.search(r'^interface (\S+)', line)
            if match_intrf:
                interface = match_intrf.group(1)
                all_interfaces.append(interface)
            match = re.search(r'^ description .+', line)
            if match:
                intrf_with_desc[interface] = match.group()
    return [intrf for intrf in all_interfaces if intrf not in intrf_with_desc.keys()]
