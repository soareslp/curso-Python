'''Verificar se com 3 comprimentos de retas dá pra formar um triângulo
e ver se são isóceles - dois lados iguais
equilátero - todos lados iguais
escaleno - nenhum lado igual'''

r1 = int(input('Digite o primeiro comprimento de reta: '))
r2 = int(input('Digite o segundo comprimento de reta: '))
r3 = int(input('Digite o terceiro comprimento de reta: '))

if r2 + r3 > r1 and r1 + r3 > r2 and r1 + r2 > r3:
    print('É possivel de formar um triângulo com essas retas')
    if r1 == r2 == r3:
        print('Por possui os três lados iguais esse é um triângulo equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Por possui dois lados iguais esse é um triângulo isóceles')
    elif r1 != r2 != r3:
        print('Por não possuir lados iguais esse é um triângulo escaleno')
else:
    print('Não é possível formar um triângulo com essas retas')