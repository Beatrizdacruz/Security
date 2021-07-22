

import random
import string

tamanho = 10
# ainda é possível gerar senhas a partir de um input, ou seja, quantos caracteres você deseja.
#estrutura da senha gerada (o ascii_letters permite as letras em qualquer formato):
chars = string.ascii_letters + string.digits + '*?!@#$%¨&'
rnd = random.SystemRandom()
print(''.join(rnd.choice(chars) for b in range(tamanho)))

