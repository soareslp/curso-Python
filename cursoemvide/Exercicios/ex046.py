'''Fazer contagem regressiva para estouro de fogos de artifício, com pausa de 1 segundo entre eles'''
from time import sleep
s = 11
for c in range(10, 0, -1):
    s -= 1
    print('{}'.format(s, sleep(1)))
print('BOOOM EXPLODIU!!!!')
