# -*- coding: utf-8 -*-
"""
Задание 19.2

Создать функцию send_show_command_to_devices, которая отправляет одну и ту же
команду show на разные устройства в параллельных потоках, а затем записывает
вывод команд в файл. Вывод с устройств в файле может быть в любом порядке.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* command - команда
* filename - имя текстового файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в обычный текстовый файл в таком формате
(перед выводом команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.2   YES NVRAM  up                    up
Ethernet0/1                10.1.1.1        YES NVRAM  administratively down down
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down

Для выполнения задания можно создавать любые дополнительные функции.

Проверить работу функции на устройствах из файла devices.yaml
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
import yaml
import netmiko
import re
from pprint import pprint



def send_show_command(device, command):
    ip = device['host']
    with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
        regex = r'.*\n(?P<prompt>R\d*#)'
        output_prompt = ssh.send_command('show', strip_prompt=False)
        match = re.search(regex, output_prompt, re.DOTALL)
        if match:
#            print(match.group('prompt'))
            prompt = match.group('prompt') + command
        else:
            print('prompt not found')
        output = prompt + '\n' + ssh.send_command(command)
        return {ip: output}



def send_show_command_to_devices(devices,command, filename, limit=3):
    data = {}
    with ThreadPoolExecutor(max_workers=limit) as executor:
        future_list = [
            executor.submit(send_show_command, device, command) for device in devices
        ]
        for f in as_completed(future_list):
            data.update(f.result())
        with open(filename, 'w') as ff:
            ff.write('\n'.join(data.values()))



if __name__ == '__main__':
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
    pprint(send_show_command_to_devices(devices, 'sh ip int br', 'result.txt'))

