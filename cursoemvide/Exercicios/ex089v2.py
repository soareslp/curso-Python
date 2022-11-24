'''LER O NOME E DUAS NOTAS DE VÁRIOS ALUNOS E GUARDAR TUDO EM UMA LISTA COMPOSTA.
MOSTRAR O BOLETIM CONTENDO A MÉDIA DE CADA UM E PERMITA O USUÁRIO POSSA MOSTRAR
AS NOTAS DE CADA ALUNO INDIVIDUALMENTE'''
alunos = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-=' * 26)
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('_' * 35)
    opc = int(input("Qual aluno? (999 interrompe)"))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(alunos) - 1:
        print(f'Notas de {alunos[opc][0]} são {alunos[opc][1]}')
print('VOLTE SEMPRE')