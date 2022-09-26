'''Fazer um Jokenpô contra o computador Saicho a Goo, Janken GUUUUUUUU Jajanken!!!!!!'''
import time
from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

print('''Escolha uma das opções:
[0] PEDRA
[1] PAPEL
[2} TESOURA''')
jogador = int(input('Qual sua escolha? '))

print('JO')
print('KEN'.format(time.sleep(0)))
print('PO!!!'.format(time.sleep(0)))
time.sleep(0)

print('-=-'*9)
print("Computador escolheu: {}".format(itens[computador]))
print('Jogador escolheu: {}'.format(itens[jogador]))
print('-=-'*9)

if computador == 0:
    if jogador == 0:
        print('Nós \033[33mEMPATAMOS!\033[3m')
    elif jogador == 1:
        print('Parabéns você \033[32mVENCEU!\033[m')
    elif jogador == 2:
        print('Que pena você \033[31mPERDEU!\033[m')

if computador == 1:
    if jogador == 0:
        print('Que pena você \033[31mPERDEU!\033[m')
    elif jogador == 1:
        print('Nós \033[33mEMPATAMOS!\033[3m')
    elif jogador == 2:
        print('Parabéns você \033[32mVENCEU!\033[m')

if computador == 2:
    if jogador == 0:
        print('Parabéns você \033[32mVENCEU!\033[m')
    elif jogador == 1:
        print('Que pena você \033[31mPERDEU!\033[m')
    elif jogador == 2:
        print('Nós \033[33mEMPATAMOS!\033[3m')
