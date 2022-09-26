'''MOSTRAR A TABUADA DE VÁRIOS NÚMEROS, UM DE CADA VEZ, PARA CADA VALOR DIGITADO
O PROGRAMA SERÁ INTERROMÍDO QUANDO O NÚMERO FOR NEGATIVO'''

while True:
    print('_'*40)
    num = int(input('Insira um número para saber sua tabuada:'))
    print('-' * 20)
    if num < 0:
        break
    for c in range(0, 10):
        c += 1
        print(f'{num} x {c} = {num*c}')
print('FIM')
