def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
    print()

def soma2(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

def contador(*num):
    print(num)

def contador2(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')

def contador3(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
        

#Programa Principal
soma(4, 5)
'''a = 4
b = 5
s = a + b
print(s)'''

soma(8, 9)
'''a = 8
b = 9
s = a + b
print(s)'''

soma(2, 1)
'''a = 2
b = 1
s = a + b
print(s)'''

soma(4, 1)

soma(a=4, b=5)
soma(b=4, a=5)

contador(2, 1, 7)
contador(8, 0)
print()

contador2(2, 1, 7)
contador2(8, 0)

contador3(2, 1, 7)
contador3(8, 0)
print()

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
print()

soma2(2, 3, 1, 6)
soma2(5, 8)
