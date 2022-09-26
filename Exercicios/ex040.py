'''Calcular as notas de um aluno e dizer se tá aprovado, reprovado ou em recuperação'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('Nota {}, você está reprovado!'.format(media))
elif media >= 5 and media < 7:
    print('Nota {}, você está em recuperação!'.format(media))
elif media >= 7:
    print('Nota {}, você está aprovado!'.format(media))