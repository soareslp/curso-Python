'''LER O NOME E DUAS NOTAS DE VÁRIOS ALUNOS E GUARDAR TUDO EM UMA LISTA COMPOSTA.
MOSTRAR O BOLETIM CONTENDO A MÉDIA DE CADA UM E PERMITA O USUÁRIO POSSA MOSTRAR
AS NOTAS DE CADA ALUNO INDIVIDUALMENTE'''
alunos = list()
lista = list()
resp = ''

while True:
    alunos.append(str(input('Nome: ')))
    alunos.append((float(input('Nota 1: '))))
    alunos.append((float(input('Nota 2: '))))
    resp = str(input('Quer continuar? [S/N]')).upper().upper()[0]
    lista.append(alunos[:])
    alunos.clear()
    if resp == 'N':
        break

print(f'{"Nº":<4}', f'{"NOME":<4}', f'{"MÉDIA":<4}')
print('_'*25)
for i, l in enumerate (lista):
    print(f'{i+1:<4}   {l[0]:<4}        {(l[1]+l[2])/2:<4}')

while True:
    switch = int(input('Mostrar notas de qual aluno? (999 para interromper)'))
    if switch in lista.index():
        print(f'Notas de {lista}')
    elif switch == 999:
        print('SAIU DO PROGRAMA!')
    elif switch not in lista:
        print('Aluno não está presente no boletim. Tente outro')
        break

