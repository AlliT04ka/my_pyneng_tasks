# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map(config_filename):
    with open(config_filename, 'r') as f:
        all_strings = f.read().split('!')
    cleared_intf_list = [a.strip().split('\n') for a in all_strings if 'interface' in a]
    access_intf = dict()
    trunk_intf = dict()
    for elem in cleared_intf_list:
        vlan = ''
        flg_access = flg_trunk = False
        cleared_elem = [a.strip() for a in elem]
        if 'switchport mode access' in cleared_elem:
            flg_access = True
        elif 'switchport mode trunk' in cleared_elem:
            flg_trunk = True
        else:
            continue
        interface = cleared_elem[0].replace('interface ', '')
        for string in cleared_elem:
            if 'vlan' in string:
                vlan = string.split()[-1].split(',')
                if len(vlan) == 1:
                    vlan = int(vlan[0])
                elif len(vlan) > 1:
                    vlan = [int(a) for a in vlan if a.isdigit()]
                break
        if interface and vlan:
            if flg_access:
                access_intf[interface] = vlan
            elif flg_trunk:
                trunk_intf[interface] = vlan
    return access_intf, trunk_intf
