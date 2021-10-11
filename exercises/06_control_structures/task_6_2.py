# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input('Input IP adress in format 10.0.1.1 : ')
ips = list(map(lambda x: int(x), ip.split('.')))
if ip == '0.0.0.0':
    msg = 'unassigned'
elif ip == '255.255.255.255':
    msg = 'local broadcast'
elif 1 <= ips[0] <= 223:
    msg = 'unicast'
elif 224 <= ips[0] <= 239:
    msg = 'multicast'
else:
    msg = 'unused'
print(msg)
