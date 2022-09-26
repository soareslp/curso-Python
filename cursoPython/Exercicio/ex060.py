'''LER UM NÚMERO E MOSTRAR SEU FAOTRIAL'''
from math import factorial

n = int(input('Digite o número que queira saber seu fatorial: '))
f = factorial(n)
c = n
while c > 0:
    print('{} x '.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print('{}'.format(f))