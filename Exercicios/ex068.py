'''JOGO DE PAR OU ÍMPAR. O JOGO SÓ PARA QUANDO O JOGADOR PERDER MOSTRANDO O TOTAL DE VITÓRIAS'''
from random import randint

print('Vamos jogar o jogo de par ou ímpar, está preparado?')
cont = 0
escolha = 0

while True:
    print('\n[0] PAR\n[1] ÍMPAR')
    escolha = int(input('O que você irá escolher? '))
    computador = randint(1, 10)
    jogador = int(input('Escolha um número: '))
    print(f'Jogador jogou {jogador} e o Computador jogou {computador}')
    if escolha == 0:
        if (jogador % 2) == (computador % 2):
            print('Jogador venceu!')
            cont += 1
        else:
            print('Jogador perdeu!')
            break
    elif escolha == 1:
        if (jogador % 2) != (computador % 2):
            print('Jogador venceu!')
            cont += 1
        else:
            print('Jogador perdeu!')
            break
print(f'\nFIM DO JOGO\nO jogador venceu {cont} vezes')

