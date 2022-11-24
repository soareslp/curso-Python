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
print(f'O maior valor da lista é: {mai} e sua posição é: {num.index(mai)+1}ª')
print(f'O menor valor da lista é: {men} e sua posição é: {num.index(men)+1}ª')