'''FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA CONTADOR(), QUE RECEBA TRÊS PARÂMETROS:
INICIO, FIM A PASSO E REALIZE A CONTAGEM.
SEU PROGRAMA TEM QUE REALIZAR TRÊS CONTAGENS ATRAVÉS DA FUNÇÃO CRIADA:
A) DE 1 ATÉ 10, DE 1 EM 1
B) DE 10 ATÉ 0, DE 2 EM 2
C) UMA CONTAGEM PERSONALIZADA'''
from time import sleep


def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} a {passo}:')
    print('------------------------------')
    if passo < 0:
        passo = passo * -1

    if passo == 0:
        passo = 1

    if inicio < fim:
        for inicio in range(inicio, fim+1, passo):
            print(f'{inicio} ', end='')
            sleep(0.5)
        print('FIM')

    elif inicio > fim:
        for fim in range(fim, inicio + 1, passo):
            print(f'{inicio} ', end='')
            inicio -= passo
            sleep(0.5)
        print('FIM')
        print()

contador(1, 10, 1)

contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
