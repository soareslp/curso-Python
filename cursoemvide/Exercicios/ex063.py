'''LER UM NÚMERO INTEIRO E MOSTRAR SUA SEQUENCIA FIBONACCI'''

n = int(input('Insira os n primeiros termos de Fibonacci: '))
c = 3
t1 = 0
t2 = 1
print('0 --> 1 ', end='')
while c <= n:
    t3 = t1 + t2
    print(' -->{}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
print('FIM')
