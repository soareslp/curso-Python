n = 1
r = 'S'
par = impar = 0
'''while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? ')).upper()
print('FIM')'''

while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('{} PARES e {} ÍMPARES'.format(par, impar))
