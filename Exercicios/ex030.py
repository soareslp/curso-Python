#Ver se um número é par ou ímpar

num = int(input('Digite um número: '))
resto = num % 2
if resto == 0:
    print('O número {} que foi digitado é par!'.format(num))
else:
    print('O número {} que foi digitado é ímpar!'.format(num))