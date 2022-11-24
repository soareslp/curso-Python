'''4 JOGADORES JOGAM UM DADO E TENHAM RESULTADOS ALEATÓRIOS.
GUARDE ESSES RESULTADO EM UM DICIONÁRIO EM ORDEM, SABENDO QUE
O VENCEDOR TIROU O MAIOR NÚMERO NO DADO
PROVAVELMENTE VAI TER QUE VER O VÍDEO'''
from random import randint
from time import sleep
from operator import itemgetter
jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)}

ranking = {}

print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} sorteou {v} no dado')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar foi {v[0]} que tirou {v[1]} no dado')
    sleep(1)
