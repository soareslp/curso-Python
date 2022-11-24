'''LER O PRIMEIRO TERMO E A RAZÃO E FAZER A P.A MOSTRANDO OS 10 PRIMEIROS TERMOS USANDO WHIILE'''

c = 0
n = int(input('O primeiro termo da P.A é: '))
r = int(input('Qual a razão? '))
while c < 9:
     n += r
     c += 1
     print('{} -->'.format(n), end='')
print('FIM')
