'''FAÇA UM MINI-SISTEMA QUE UTILIZE O INTERACTIVE HELP DO PHYTON.
O USUÁRIO VAI DIGITAR O COMANDO E O MANUAL VAI APARECER. QUANDO
O USUÁRIO DIGITAR A PALAVRA 'FIM', O PROGRAMA SE ENCERRARÁ.
OBS: USE CORES.'''


def ajuda(msg):
    print('\033[7;32;44m~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'Acessando o manual do comando {msg}')
    print('~~~~~~~~~~~~~~~~~~~~~~~')
    print('\033[m')
    print('\033[1;35;43m')
    print(help(msg))
    print('\033[m')


#Programa Principa
comando = ''
while True:
    print('\033[7;30;42m~~~~~~~~~~~~~~~~~~~~~~~')
    print('Sistema de ajuda PyHELP')
    print('~~~~~~~~~~~~~~~~~~~~~~~')
    print('\033[m')
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)