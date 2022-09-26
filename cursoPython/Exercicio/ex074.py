'''Gerar cinco números aleatórios e colocar em uma tupla.
mostrar a listagem de números também o maior e menor'''
from random import randint

n1 = randint(0, 10)
n2 = randint(0, 10)
n3 = randint(0, 10)
n4 = randint(0, 10)
n5 = randint(0, 10)
maior = menor = n1

if maior < n2:
    maior = n2
elif maior < n3:
    maior = n3
elif maior < n4:
    maior = n4
elif maior < n5:
    maior = n5


if menor > n2:
    menor = n2
elif menor > n3:
    menor = n3
elif menor > n4:
    menor = n4
elif menor > n5:
    menor = n5
num = (n1, n2, n3, n4, n5)
print(f'Os valores sorteados foram {num}')
print(f'O {maior} é o maior e {menor} é o menor')

