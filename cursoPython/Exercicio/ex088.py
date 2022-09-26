'''FAÇA UM PROGRAMA QUE DE PALPITES PARA O JOGO DA MEGA SENA. O PROGRAMA VAI PERGUNTAR QUANTOS JOGOS SERÃO GERADOS E
VAI SORTEAR 6 NÚMEROS ENTRE 1 E 60 PARA CADA JOGO, CADASTRANDO TUDO EM UMA LISTA COMPOSTA'''
from random import randint
jogo = list()
lista = list()

quant = int(input('Quantos jogos sortear? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont >= 6:
            break
    jogo.sort()
    lista.append(jogo[:])
    jogo.clear()
    tot += 1
for i, l in enumerate (lista):
    print(f'Jogo {i+1}: {l}')
