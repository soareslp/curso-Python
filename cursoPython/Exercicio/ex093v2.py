'''GERENCIAR O APROVEITAMENTO DE UM JOGADOR DE FUTEBOL.
LER NOME DO JOGADOR, QUANTAS PARTIDAS ELE JOGOU. DEPOIS
VAI LER A QUANTIDADE DE GOLS FEITOS EM CADA PARTIDA. NO FINAL,
TUDO ISSO SERÁ GUARDADO EM UM DICIONÁRIO, INCLUINDO O TOTAL
DE GOLS FEITOS DURANTE O CAMPEONATO.'''
jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Quantas partidas foram jogadas? '))

for p in range(0, partidas):
    gols.append(int(input(f'    Quantos gols na partida {p+1}? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-=' * 25)
print(jogador)
print('-=' * 25)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 25)

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')

for i, v in enumerate(jogador['gols']):
    print(f'    =>Na partida {i+1}, fez {v}')
print(f'Foi um total de {jogador["total"]} gols')
