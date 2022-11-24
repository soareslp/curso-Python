'''APRIMORAR O DESAFIO ANTERIOR, MOSTRANDO:
A) A SOMA DE TODOS OS VALORES PARES DIGITADOS
B) A SOMA DA TERCEIRA COLUNA
C) O MAIOR VALOR DA SEGUNDA LINHA'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = somaTerc = maiorSegunda = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^6}]', end='')
        if matriz[l][c] % 2 == 0:
            somaPar += matriz[l][c]
        if c == 2:
            somaTerc += matriz[l][c]
        if l == 1:
            if matriz[l][c] > maiorSegunda:
                maiorSegunda = matriz[l][c]
    print()


print(f'A soma dos valores pares são: {somaPar}')
print(f'A soma dos valores da terceira coluna são: {somaTerc}')
print(f'O maior valor da segunda linha é: {maiorSegunda}')

