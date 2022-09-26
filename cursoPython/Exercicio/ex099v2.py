'''FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA MAIOR(), QUE RECEBA VÁRIOS PARÂMETROS COM
VALORES INTEIROS. SEU PROGRAMA TEM QUE ANALISAR TODOS OS VALORES E DIZER QUAL DELES É O MAIOR'''
from time import sleep


def maior(*num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor foi o {maior}.')
    print('-=' * 25)
    print()



maior(1, 6, 7, 3)
maior(2, 9)
maior(1)
maior()