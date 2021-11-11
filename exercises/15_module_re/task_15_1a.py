# -*- coding: utf-8 -*-
"""
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом,
чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""
import re


def get_ip_from_cfg(file_name):
    result = dict()
    regex = re.compile(r'interface\s(\w.+)')
    with open(file_name, 'r') as f:
        for line in f:
            match_int = regex.search(line)
            if match_int:
                interface = match_int.group(1)
            match = re.search(r' ip address\s(?P<ip>\d+\.\d+.\d+\.\d+)\s(?P<mask>\d+\.\d+\.\d+\.\d+)', line)
            if match:
                result[interface] = ((match.group('ip'), match.group('mask')))
    return result
