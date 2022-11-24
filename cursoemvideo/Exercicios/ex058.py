'''FAZER UM JOGO QUE O COMPUTADOR PENSE EM UM NÚMERO DE 0 A 10 E O JOGADOR TENTA ADIVINHAR, MOSTRAR NO FINAL
QUANTAS CHANCES FORAM NECESSÁRIAS PARA CONSEGUIR'''
from random import randint
tot = 0
computador = randint(0, 10)
print('Acabei de escolher um número de 0 a 10, tente adivinha-lo')
jogador = int(input('Esolha um número:'))

while jogador != computador:
    if jogador > computador:
        tot += 1
        jogador = int(input('Menos... Tente novamente!\nEscolha um número: '))
        tot += 1
    if jogador < computador:
        tot += 1
        jogador = int(input('Mais... Tente novamente!\nEscolha um número: '))
        tot += 1
print('Parabéns o número sorteado foi {}, voce precisou de {} tentativas!!!'.format(computador, tot))
