# -*- coding: utf-8 -*-
"""
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

"""
import re


def parse_sh_ip_int_br(file_name):
    with open(file_name, 'r') as f:
        match = re.findall(r'(?P<interface>\S+\d)\s+'
                           r'(?P<ip>\S+)\s+\w+\s+\w+\s+'
                           r'(?P<status>\S+\s?\w*)\s*'
                           r'(?P<protocol>\S+)', f.read())
        return [(intr, ip , status.strip(), proto) for intr, ip, status, proto in match]
