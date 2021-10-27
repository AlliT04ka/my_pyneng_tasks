# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
import ipaddress


def convert_ranges_to_ip_list(ip_list):
    correct_ip_list = []
    for elem in ip_list:
        splited_elem = elem.split('-')
        if len(splited_elem) > 1:
            ip1, part2 = splited_elem
            correct_ip_list.append(ip1)
            first_ip = ipaddress.ip_address(ip1)
            if part2.isdigit():
                last_num = int(part2)
            else:
                last_num = int(part2.split('.')[3])
            first_num = int(ip1.split('.')[3])
            for n in range(1, last_num - first_num + 1):
                next_ip = first_ip + n
                correct_ip_list.append(str(next_ip))
        elif len(splited_elem) == 1:
            correct_ip_list.append(splited_elem[0])
    return correct_ip_list
