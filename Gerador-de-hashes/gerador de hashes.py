import hashlib

string = input('Insira o texto a ser gerado a hash: ')
menu = int(input('''## MENU- ESCOLHA O TIPO DE HASH ### \n1)MD5\n2)SHA1\n3)SHA256\nInsira sua opção: '''))

if menu == 1:
    result = hashlib.md5(string.encode('utf-8'))
    print(f'o hash da string {string} é: ', result.hexdigest())
elif menu == 2:
    result = hashlib.sha1(string.encode('utf-8'))
    print(f'o hash da string {string} é: ', result.hexdigest())
elif menu == 3:
    result = hashlib.sha256(string.encode('utf-8'))
    print(f'o hash da string {string} é: ', result.hexdigest())
else:
    print('Algo deu errado. Tente novamente.')