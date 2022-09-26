'''LER VÁRIOS NÚMEROS E COLOCAR NA LISTA.
MOSTRAR:
A) QUANTOS NÚMEROS FORAM DIGITADOS
B) ORDERNAÇÃO DECRESCENTE
C) SE O VALOR 5 FOI DIGITADO E ESTÁ OU NÃO NA LISTA'''
lista = []
resp = ''
while True:
    atual = int(input('Digite um número: '))
    lista.append(atual)
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
lista.sort(reverse=True)
print(f'Você digitou {len(lista)+1} elementos')
print(f'Os valores em ordem decrescente são: {lista}')
print(f'O número 5 apareceu na lista' if 5 in lista else 'O número 5 não aparece na lista')
