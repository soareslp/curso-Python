'''LER O NOME E PESO DE VÁRIAS PESSOAS, GUARDANDO EM UMA LISTA E MOSTRAR:
A) QUANTAS PESSOAS FORAM CADASTRADAS
B) LISTAGEM COM AS PESSOAS MAIS PESADAS
C) LISTAGEM COM AS PESSOAS MAIS LEVES'''
pessoas = []
galera = []
pesadas = []
leves = []
pesoMaior = pesoMenor = quant = 0
while True:
    pessoas.append(str(input('Digite o nome: ')))
    pessoas.append(float(input('Digite o peso: ')))
    if len(galera) == 0:
        pesoMaior = pesoMenor = pessoas[1]
    else:
        if pessoas[1] > pesoMaior:
            pesoMaior = pessoas[1]
        if pessoas[1] < pesoMenor:
            pesoMenor = pessoas[1]
    galera.append(pessoas[:])
    pessoas.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    quant += 1
    if resp == 'N':
        break


print(f'Foram cadastradas {quant} pessoas')
print(f'O maior peso foi de {pesoMaior}Kg, das pessoas ', end='')
for g in galera:
    if pesoMaior == g[1]:
        print(f'{g[0]}', end=', ')
print(f'\nO menor peso foi de {pesoMenor}Kg, das pessoas ', end='')
for g in galera:
    if pesoMenor == g[1]:
        print(f'{g[0]}', end=', ')

