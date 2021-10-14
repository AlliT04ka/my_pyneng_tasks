# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
import sys


ignore = ["duplex", "alias", "configuration"]
if sys.argv[1] is None:
    sys.exit()
with open(sys.argv[1], 'r') as f, open(sys.argv[2], 'w') as dest:
    for line in f:
        flg_ignore = False
        for elem in ignore:
            if elem in line:
                flg_ignore = True
                continue
        if not line.startswith('!') and not flg_ignore:
            dest.write(line)


