#Ler a velocidade de um carro, se ultrapassar 80km/h falar que foi multado em R$7,00 por cada km a acima do limite

vel = int(input('Insira a velocidade do carro: '))
if vel <= 80:
    print('Velocidade do carro é de {}'.format(vel))
else:
    multa = (vel - 80) * 7
    print('Por ultrapassar a velocidade máxima permitida em {}km/h, você receberá uma multa de R${},00'.format(vel-80, multa))