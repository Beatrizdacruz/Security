#Com a utilização da biblioteca OS do python, este módulo oferece de uma maneira simples de usar funcionalidades que
# são dependentes de sistema operacional. Então utilizaremos dessa biblioteca para chamar o ping e fazer as modificações.
import os

#criar variável para receber o IP ou host para o pig
print('-=' * 30)
ip_host = input('Digite o IP ou host a ser verificado: ')
print('-=' * 30)

# passar o ip para o ping:
os.system(f'ping -n 6 {ip_host}')
