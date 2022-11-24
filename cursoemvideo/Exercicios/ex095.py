'''APRIMORE O DESAFIO 093 PARA QUE ELE FUNCIONE COM VÁRIOS JOGADORES, INCLUINDO
UM SISTEMA DE VISUALIZAÇÃO DE DETALHES DO APROVEITAMENTO DE CADA JOGADOR'''
time = []
jogador = dict()
gols = list()
resp = ''

while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input('Quantas partidas foram jogadas? '))
    for p in range(0, partidas):
        gols.append(int(input(f'    Quantos gols na partida {p+1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    gols.clear()
    resp = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    time.append(jogador.copy())
    if resp == 'N':
        break
print()
print('-=' * 40)
print(f'{"cod":<3} {"nome":<7} {"gols":<8} {"total"}')
print('-' * 40)

for i in range(0, len(time)):
    print(f'{i} {time[i]["nome"]:<4} {time[i]["gols"]} {time[i]["total"]}')
print()
while True:
    resp = int(input('Quer mostrar dados de qual jogador? (999 para parar) '))
    if 0 >= resp <= len(time) or resp == 999:
        if resp == 999:
            break
        else:
            print(f' -- LEVANTAMENTO DO JOGADOR {time[resp]["nome"]} --')
            for i, v in enumerate(time[resp]["gols"]):
                print(f'No jogo {i} fez {v} gols.')
    else:
        print('Jogador não cadastrado. Tente novamente: ')
print('>>>>  FIM  <<<<')
