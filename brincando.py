# importando bibliotecas
from random import randint
from time import sleep

# gerando número aleatório
n = randint(1, 52)

# repassando o número para o usuário e esperando 1 segundo
print(f'Eu escolhi o número {n}, iremos trabalhar com ele.')
sleep(1)

# função de soma
def soma(a):
    return a + a

# função de multiplicação
def multiplicacao(a):
    return a * a

# função do expoente 2
def expoente_2(a):
    dois = 1
    for i in range(a):
        dois *= 2
    return dois

# função de fatorial
def fatorial(a):
    n = 1
    for i in range(1, a+1):
        a = i * n
        n = a
    return a

# função do expoente próprio
def expoente_proprio(a):
    n = a
    for i in range(0, a-1):
        a = a * n
    return a

# expondo na tela
print(f'''{n} + {n} = {soma(n)}
{n} x {n} = {multiplicacao(n)}
2 ^ {n} = {expoente_2(n)}
{n}!    = {fatorial(n)}
{n} ^ {n} = {expoente_proprio(n)}
''')
