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
    print()

print(f'A soma dos valores pares são: {somaPar}')

for l in range(0, 3):
        somaTerc += matriz[l][2]
print(f'A soma dos valores da terceira coluna são: {somaTerc}')

for c in range(0, 3):
    if c == 0:
        maiorSegunda = matriz[1][c]
    elif matriz[1][c] > maiorSegunda:
        maiorSegunda = matriz[1][c]
print(f'O maior valor da segunda linha é: {maiorSegunda}')
