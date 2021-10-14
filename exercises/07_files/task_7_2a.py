# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
import sys


ignore = ["duplex", "alias", "configuration"]
if sys.argv[1] is None:
    sys.exit()
with open(sys.argv[1], 'r') as f:
    for line in f:
        flg_ignore = False
        for elem in ignore:
            if elem in line:
                flg_ignore = True
                continue
        if not line.startswith('!') and not flg_ignore:
            print(line, end='')

