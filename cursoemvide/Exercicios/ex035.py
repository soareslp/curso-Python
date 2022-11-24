#Verificar se com 3 comprimentos de retas dá pra formar um triângulo

r1 = int(input('Digite o primeiro comprimento de reta: '))
r2 = int(input('Digite o segundo comprimento de reta: '))
r3 = int(input('Digite o terceiro comprimento de reta: '))

if r2 + r3 > r1 and r1 + r3 > r2 and r1 + r2 > r3:
    print('É possivel de formar um triângulo com essas retas')
else:
    print('Não é possível formar um triângulo com essas retas')