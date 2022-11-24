'''LER NÚMEROS E FAZER A MÉDIA E QUAL O VALOR MAIOR E QUAL O MENOR, PERGUNTAR SE QUER CONTINUAR A LER'''

soma = cont = n = maior = 0
menor = 99999999999
var = ''

while var != 'N':
    n = int(input('Digite um número: '))
    soma += n
    cont+=1
    var = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print('Foram realizadas {}x o maior número é {} e o menor é {}'.format(cont, maior, menor))
print('A média foi {}'.format(soma/cont))
