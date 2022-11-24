'''LER O PRIMEIRO TERMO E A RAZÃO DE UMA P.A E MOSTRAR OS 10 PRIMEIROS TERMOS'''
n = int(input('O primeiro termo da P.A é: '))
r = int(input('Qual a razão? '))
s = 0

for c in range(0, 10):
    n += r
    print('{}'.format(n))
