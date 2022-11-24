'''LER NOME, SEXO E IDADE DE VÁRIAS PESSOAS. GUARDANDO OS DADOS
DE CADA PESSOA EM UM DICIONÁRIO E TODOS OS DICIONÁRIOS EM UMA LISTA.
NO FINAL, MOSTRE:
A) QUANTAS PESSOAS FORAM CADASTRADAS
B) A MÉDIA DE IDADE DO GRUPO
C) UMA LISTA COM TODAS AS MULHERES.
D) UMA LISTA COM TODAS AS PESSOAS COM IDADE ACIMA DA MÉDIAS'''

pessoas = {}
lista = []
nomeM = []
nomeMaior = []
sexo = resp = ''
totIdade = 0

while True:
    pessoas['nome'] = str(input('Nome: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if sexo not in "MF":
        print('ERRO! Por favor, digite apenas M ou F.')
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    pessoas['sexo'] = sexo
    pessoas['idade'] = int(input('Idade: '))
    resp = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    lista.append(pessoas.copy())
    if resp == 'N':
        break
print('-=' * 35)
print(lista)
print('-=' * 35)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas')

for l in range(0, len(lista)):
    totIdade += lista[l]['idade']
media = totIdade/len(lista)
print(f'B) A média de idade do grupo é {media}')


print(f'C) As mulheres do grupo são:', end=' ')
for l in range(0, len(lista)):
    if lista[l]['sexo'] == 'F':
        nomeM.append(lista[l]['nome'])
        print(f'{lista[l]["nome"]} ', end='')


print(f'\nD) Lista de pessoas maiores de idade é:')
for l in range(0 , len(lista)):
    if lista[l]['idade'] >= 18:
        print(f'    Nome = {lista[l]["nome"]:<9} Sexo = {lista[l]["sexo"]:<9} Idade = {lista[l]["idade"]:<9}')
