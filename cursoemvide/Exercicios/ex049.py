'''FAZER A TABUADA DE UM NÚMERO USANDO FOR'''
n = int(input('Digite o número que deseja ver sua tabuada: '))
for c in range (1, 11):
    print('{} x {} = {}'.format(n, c, n*c))
