import random

a1 = input('Nome: ')
a2 = input('Nome: ')
a3 = input('Nome: ')
a4 = input('Nome: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem será: ')
print(lista)

