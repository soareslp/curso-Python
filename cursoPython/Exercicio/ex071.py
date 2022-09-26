'''SIMULAR CAIXA ELETRÔNICO. PERGUNTAR O VALOR A SER SACADO (INT)
E O COMPUTADOR VAI INFORMAR AS CÉDULAS QUE SERÃO ENTREGUES.
CÉDULAS: 50, 20, 10 E 1'''

valor = int(input('Qual valor você quer sacar? R$'))
cinquenta = vinte = dez = um = 0

cinquenta = valor // 50
valor -= 50*cinquenta
vinte = valor // 20
valor -= 20*vinte
dez = valor // 10
valor -= 10 * dez
um = valor

print(f'Total de {cinquenta} cédulas de 50 reais\nTotal de {vinte} cédulas de 20 reais\nTotal de {dez} cédulas de 10 reais'
      f'\nTotal de {um} cédulas de 1 real')