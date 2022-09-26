'''LER VÁRIOS NÚMEROS INTEIROS . PROGRAMA SÓ PARA QUANDO LER 999.
NO FINAL MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS E QUAL A SOMA DELES'''

cont = soma = 0

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A soma dos {cont} números digitados foi {soma}')