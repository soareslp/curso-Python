'''Ler um número inteiro e o usuário escolher qual a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal'''
num = int(input('Digite um número inteiro qualquer: '))
escolha = int(input('Escolher uma entre as opções de conversão:\nDigite 1 para binário\nDigite 2 para octal\nDigite 3 '
                    'para hexadecimal\nEscolha a opção:'))
if escolha == 1:
    print('O número {} digitado por você em binário é: {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('O número {} digitado por você em octal é: {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('O número {} digitado por você em hexadecimal é: {}'.format(num, hex(num)[2:]))
else:
    print('Escolha inválida!')