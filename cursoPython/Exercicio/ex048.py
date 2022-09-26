'''SOMA DOS NÚMERO MÚLTIPLOS DE 3 ENTRE 1 E 500'''
s = 0
for c in range(1, 500):
    if(c % 3 == 0 and c % 2 == 1):
        print('Múltiplos de 3: {}'.format(c))
        s += c
print(s)