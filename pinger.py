# Простой скрипт для пинга хостов и формирования ansible inventory. 
# На вход подается текстовый файл с набором dns имен хостов. Каждый хост пингуется. На выходе формируется ansible inventory

import subprocess
import re

hosts = []

with open('C:\Work\Automatization\inventory.txt', 'r') as f:
    for line in f:
        line = line.strip()  # удаляем пробелы и символы переноса строки
        hosts.append(line)

print(hosts)

with open('C:\Work\Automatization\/result.txt', 'w') as f:
    for h in hosts:
        ping = subprocess.Popen(["ping", "-n", "1", "-w", "200", h],
            stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        out, error = ping.communicate()
        print(out.decode('cp866'))
        ip_list = re.findall(r'\d+\.\d+\.\d+\.\d+', out.decode('cp866'))
        if len(ip_list) > 0:
            ip = ip_list[0]
        else:
            ip = 'unreachable'
        output = f"{h} ansible_ssh_host={ip} ansible_ssh_user=sadmin\n"
        f.write(output)
