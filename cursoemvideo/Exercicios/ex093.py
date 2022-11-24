'''GERENCIAR O APROVEITAMENTO DE UM JOGADOR DE FUTEBOL.
LER NOME DO JOGADOR, QUANTAS PARTIDAS ELE JOGOU. DEPOIS
VAI LER A QUANTIDADE DE GOLS FEITOS EM CADA PARTIDA. NO FINAL,
TUDO ISSO SERÁ GUARDADO EM UM DICIONÁRIO, INCLUINDO O TOTAL
DE GOLS FEITOS DURANTE O CAMPEONATO.'''
jogador = dict()
gols = list()
tot = 0
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Quantas partidas foram jogadas? '))

for p in range(0, partidas):
    gols.append(int(input(f'    Quantos gols na partida {p+1}? ')))
    tot += gols[p]
jogador['gols'] = gols
jogador['total'] = tot
print('-=' * 25)
print(jogador)
print('-=' * 25)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 25)

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')

for g in range(0, len(gols)):
    print(f'    =>Na partida {g+1}, fez {gols[g]}')
print(f'Foi um total de {tot} gols')
