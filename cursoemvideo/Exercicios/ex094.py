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
totIdade = totM = totMIdade = 0

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
    if lista[l]['sexo'] == 'F':
        totM +=1
        nomeM.append(lista[l]['nome'])
    if lista[l]['idade'] >= 18:
        totMIdade += 1
        nomeMaior.append(lista[l]['nome'])
media = totIdade/len(lista)
print(f'B) A média de idade do grupo é {media}')
print(f'C) O total de mulheres do grupo é {totM} são: {nomeM}')
print(f'D) O total de pessoas maiores de idade é {totMIdade} são {nomeMaior}')


