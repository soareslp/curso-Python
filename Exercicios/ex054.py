'''LER O ANO DE NASCIMENTO DE 7 PESSOAS. MOSTRAR QUANTAS TEM 18 ANOS OU MAIS E QUNTAS NÃO'''
from datetime import date
atual = date.today().year
totMaior = 0
totMenor = 0
for pessoa in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoas nasceu? '.format(pessoa)))
    idade = atual - nasc
    if idade >= 18:
        totMaior += 1
    else:
        totMenor += 1
print('A quantidade de pessoas MAIOR de IDADE são: {}'.format(totMenor))
print('A quantidade de pessoas MAIOR de IDADE são: {}'.format(totMaior))
