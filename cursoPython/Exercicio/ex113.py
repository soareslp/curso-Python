'''Reescreva a função leiaInt() que fizemos  no dsafio 104 agora com a possibilidade da digitação de um
número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcinalidade'''

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Por favor digite um valor inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\33[31mO usuário preferiu não informar os dados!\33[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Por favor digite um valor real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\33[31mO usuário preferiu não informar os dados!\33[m')
            return 0
        else:
            return n


n1 = leiaInt('Digite um inteiro: ')
n2 = leiaFloat('Digite um real: ')
print(f'O valor inteiro digitado foi {n1} e real foi {n2}')