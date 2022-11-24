num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
num.pop(3)
num.remove(2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')

valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei no final da lista!')

valor = list()
for cont in range(0, 5):
    valor.append(int(input('Digite um valor: ')))
for c, v in enumerate(valor):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei no final da lista!')

a = [2, 3, 4, 7]
'''b = a
print(f'Lista A: {a}')
print(f'Lista B: {b}\n')

b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}\n')'''

b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
