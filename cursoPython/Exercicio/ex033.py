#Ler três números e ver qual é o maior e o menor
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 > n2 > n3:
    print('{} é o maior número, e o {} é menor'.format(n1, n3))

elif n1 > n3 > n2:
    print('{} é o maior número, e o {} é menor'.format(n1, n2))

elif n2 > n1 > n3:
    print('{} é o maior número, e o {} é menor'.format(n2, n3))

elif n2 > n3 > n1:
    print('{} é o maior número, e o {} é menor'.format(n2, n1))

elif n3 > n1 > n2:
    print('{} é o maior número, e o {} é menor'.format(n3, n2))

elif n3 > n2 > n1:
    print('{} é o maior número, e o {} é menor'.format(n3, n1))