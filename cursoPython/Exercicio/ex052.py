'''LER UM NÚMERO INTEIRO E VER SE ELE É PRIMO'''
n = int(input('Digite um número: '))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end='')
        tot+=1
    else:
        print('\033[m', end='')
    print("{} ".format(c), end='')
print('\nO número {} foi divisível {} vezes'.format(n, tot))
if tot == 2:
    print('Número é PRIMO')
else:
    print('Número NÃO é primo')
