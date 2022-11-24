'''Pegar dois números inteiros e comparar qual é maior, menor ou se são iguais'''
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O primeiro número digitado {} é maior que o segundo número {}'.format(n1, n2))
elif n2 > n1:
    print('O segundo número digitado {} é maior que o primeiro número {}'.format(n2, n1))
else:
    print('Os dois são iguais'.format(n1, n2))