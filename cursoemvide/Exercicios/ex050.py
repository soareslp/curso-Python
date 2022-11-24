'''Ler seis número inteiros e fazer a soma dos que forem PARES'''
s = 0
for c in range(1, 7):
    d = int(input('Digite um número: '))
    if d % 2 == 0:
        s += d
print(s)