'''FAÇA UM PROGRAMA QUE LEIA O NOME E MÉDIA DE UM ALUNO,
GUARDANDO TAMBÉM A SITUAÇÃO EM UM DICIONÁRIO. NO FINAL,
MOSTRE O CONTEÚDO DA ESTRUTURA NA TELA'''
alunos = dict()
alunos['nome'] = str(input('Nome: '))
alunos['media'] = float(input(f'Média de {alunos["nome"]}: '))
if alunos['media'] >= 7:
    alunos['situacao'] = 'Aprovado'
elif 4 <= alunos['media'] < 7:
    alunos['situacao'] = 'Recuperação'
elif alunos['media'] < 4:
    alunos['situacao'] = 'Reprovado'

for k, v in alunos.items():
    print(f'{k} é igual a {v}')
