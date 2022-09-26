'''DIGITAR SETE VALORES NUMÉRICOS E CADASTRA-LOS EM UMA LISTA ÚNICA QUE MANTENHAM SEPARADOS OS VALORES PARES E ÍMPARES.
MOSTRAR OS VALORES PARES E ÍMPARES EM ORDEM CRESCENTE'''
num = [[], []]

for c in range(0, 7):
    n = int(input(f'Digite o {c+1}º número: '))
    if n % 2 == 0:
        num[0].append(n)
    elif n % 2 == 1:
        num[1].append(n)
num[0].sort()
num[1].sort()
print(num[0])
print(num[1])
