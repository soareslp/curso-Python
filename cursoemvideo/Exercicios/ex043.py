'''Cálculo de IMC e dizer se a pessoa está:
Abaixo do peso abaixo de  18.5
Peso Ideal entre 18.5 até 25
Sobre peso entre 25 até 30
Obesidade entre 30 e 40
Obesidade Mórbida mais que 40'''

peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('Digite sua altura m: '))
imc = peso/(altura**2)
print('O seu IMC é: {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso\33[m')
elif 18.5 <= imc < 25:
    print('Você está no \33[33mpeso ideal\33[m')
elif 25 <= imc < 30:
    print('Você está com \33[34msobre peso\33[m')
elif 30 <= imc < 40:
    print('Você está \33[35mobeso\33[m')
elif imc > 40:
    print('Você está com \33[31mobesidade mórbida\33[m')
