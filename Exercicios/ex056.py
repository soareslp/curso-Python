'''LER O NOME, IDADE E SEXO DE 4 PESSOAS E DIZER A MÉDIA DE IDADE, NOME DO HOMEM MAIS VELHO,
QUANTAS MOLHERES TEM MENOS DE 20 ANOS DE IDADE'''

media = 0
velho = 0
totMulher = 0
nomeVelho = ''

for p in range(1, 5):
    nome = str(input('\nDigite o nome da {} pessoa: '.format(p))).strip()
    idade = int(input('Digite a idade da {} pessoa: '.format(p)))
    sexo = str(input('Digite o sexo da {} pessoa: '.format(p))).strip()
    media += idade
    if p == 1 and sexo == 'M':
        velho += idade
        nomeVelho = nome
    if idade > velho and sexo in 'Mm':
        velho = idade
        nomeVelho = nome
        if sexo == 'F' and idade < 20:
            totMulher += 1
media = media / 4
print('\nQuantidade de mulheres abaixo de 20 anos: {}'.format(totMulher))
print('Média de idade das pessoas {}'.format(media))
print('Mais velho tem {} anos e se chama {}'.format(velho, nomeVelho))
