# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
while True:
    ip = input('Input IP adress in format 10.0.1.1 : ')
    try:
        ips = list(map(lambda x: int(x), ip.split('.')))
    except ValueError:
        print('Неправильный IP-адрес')
    else:
        if not (len(ips) == 4 and len([x for x in ips if 0 <= x <= 255]) == 4):
            print('Неправильный IP-адрес')
        else:
            break
if ips == [0, 0, 0, 0]:
    msg = 'unassigned'
elif ips == [255, 255, 255, 255]:
    msg = 'local broadcast'
elif 1 <= ips[0] <= 223:
    msg = 'unicast'
elif 224 <= ips[0] <= 239:
     msg = 'multicast'
else:
     msg = 'unused'
print(msg)
