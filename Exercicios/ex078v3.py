num = list()
mai = men =  0
for c in range(0, 5):
    num.append(int(input('Digite um número: ')))
    if c == 0:
        mai = men = num[c]
    else:
        if num[c] > mai:
            mai = num[c]
        elif num[c] < men:
            men = num [c]
print(f'Você digitou: {num}')
print(f'O maior valor da lista é: {mai} nas posições ', end='')
for i, v in enumerate(num):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor da lista é: {men} nas posicões ', end='')
for i, v in enumerate(num):
    if v == men:
        print(f'{i}...', end='')
