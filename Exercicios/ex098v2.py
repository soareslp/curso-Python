'''FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA CONTADOR(), QUE RECEBA TRÊS PARÂMETROS:
INICIO, FIM A PASSO E REALIZE A CONTAGEM.
SEU PROGRAMA TEM QUE REALIZAR TRÊS CONTAGENS ATRAVÉS DA FUNÇÃO CRIADA:
A) DE 1 ATÉ 10, DE 1 EM 1
B) DE 10 ATÉ 0, DE 2 EM 2
C) UMA CONTAGEM PERSONALIZADA'''
from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    print("-=" * 20)
    print(f'Contagem de {i} até {f} de {p} a {p}:')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{c} ', end='')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{c} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM!')


contador(1, 10, 1)
contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)