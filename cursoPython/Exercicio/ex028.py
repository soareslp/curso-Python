#Fazer o computador escolher um número de 0 a 5 e pedir pro usuário chutar qual que é
import random
from time import sleep
print('Irei escolher um número de 0 a 5')
sorteio = random.choice([0,1,2,3,4,5])
print(sorteio)
escolha = int(input('Escolha o número sorteado: '))
print('PROCESSANDO...')
sleep(3)
if escolha < 0 or escolha > 5:
    escolha = int (input('O número que você escolheu foi inválido! Digite um número de 0 a 5 novamente: '))
if escolha == sorteio:
    print('Você acertou! O número sorteado foi {}, PARABÉNS!!'.format(sorteio))
else:
    print('Infelizmente você errou! O número sorteado foi {}'.format(sorteio))



