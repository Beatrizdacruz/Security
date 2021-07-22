#o objetivo é fazer ping em diversos hosts ou diversos IP's.
import os
import time

#abrir o arquivo de texto (hosts.txt), pois lá estão os endereços.
with open('hosts.txt') as file:
    arquivo = file.read()
    arquivo = arquivo.splitlines()

    for ip in arquivo:
        os.system(f'ping -n 2 {ip}')
        print('-=' * 30)
        time.sleep(0.5)