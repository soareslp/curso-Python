'''MELHORAR O 61, PERGUNTAR SE QUER PARA, DIGITAR 0 SE SIM'''

c = 0
n = int(input('O primeiro termo da P.A é: '))
r = int(input('Qual a razão? '))
total = 0
mais = 10
while mais != 0:
    total += mais
    while c < total:
        n += r
        c += 1
        print('{} -->'.format(n), end='')
    print('PAUSA')
    mais = int(input('Quantos termos você quer a mais?'))
print('FIM! Foram mostrados {} termos'.format(total))