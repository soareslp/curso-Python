'''LER QUATRO VALORES NO TECLADO E ARMAZENAR NUMA TUPLA E MOSTRAR.
QUANTAS VEZES APARECE O 9
EM QUE POSIÇÃO APARECEU O 3
QUAIS FORAM OS NÚMEROS PARES'''

par = 0
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))
num = (n1, n2, n3, n4)

for c in range(0, 4):
    print(num[c], end='')
    if num[c] % 2 == 0:
        par += 1
print(f'\nO número 9 aparace {num.count(9)} vezes')
print(f'O número 3 aparece na posição {num.index(3)}')
print(f'Nessa tupla existem {par} números pares')
