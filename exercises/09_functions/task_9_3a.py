# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

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
            elif flg_access and 'duplex auto' in string:
                vlan = 1
                break
        if interface and vlan:
            if flg_access:
                access_intf[interface] = vlan
            elif flg_trunk:
                trunk_intf[interface] = vlan
    return access_intf, trunk_intf

