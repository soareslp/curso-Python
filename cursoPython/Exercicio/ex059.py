'''LER DOIS NÚMEROS E MOSTRAR O MENU:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA'''

inp = 0
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

while inp != 5:
    print('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA\n''')
    inp = int(input('Digite uma das opções: '))
    if inp == 1:
        print('A SOMA de {} + {} resultou em {}\n'.format(n1, n2, (n1 + n2)))
    elif inp == 2:
        print('O PRODUTO de {} x {} resultou em {}\n'.format(n1, n2, (n1 * n2)))
    elif inp == 3:
        if n1 > n2:
            print('O {} é maior que {}\n'.format(n1, n2))
        elif n2 > n1:
            print('O {} é maior que {}\n'.format(n2, n1))
        else:
            print('Os dois valem {}\n'.format(n1))
    elif inp == 4:
        print('Por favor, digite os novos números:')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    else:
        print('Opção inválida! Tente novamente')
print('FIM!')

