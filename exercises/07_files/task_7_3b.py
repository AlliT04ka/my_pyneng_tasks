# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
vlan = int(input('Input vlan number: '))
result = []
with open('CAM_table.txt', 'r') as f:
    for line in f:
        #print(line)
        if 'DYNAMIC' in line:
            result.append(line.split())
            result = list(map(lambda x: [int(x[0]),] + x[1:], result))
result.sort()
for elem in result:
    if vlan == elem[0]:
        print("{:<9}{:20}{}".format(elem[0], elem[1], elem[3]))
