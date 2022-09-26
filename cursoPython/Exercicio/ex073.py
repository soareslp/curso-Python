'''FAZER TUPLA DO BRASILEIRÃO E MOSTRAR:
5 PRIMEIROS COLOCADOS
4 ÚLTIMOS COLOCADOS
ORDEM ALFABÉTICA
QUAL POSIÇÃO O FLAMENGO TÁ'''

brasileirao = ('Corinthians', 'Palmeiras', 'Atlético-MG', 'América-MG', 'Coritiba', 'Athletico-PR', 'São Paulo',
               'Internacional', 'Santos', 'Botafogo', 'Flamengo', 'Goiás', 'Fluminense', 'Avaí', 'Cuiabá',
               'Ceará', 'Juventude', 'Bragantino', 'Atélico-GO', 'Fortaleza')
print(brasileirao)
print('Os 5 primeiros colocados são:')
for c in range(0, 5):
    print(f'{brasileirao[c]}')

print('Os 4 últimos colocados são:')
for c in range(16, 20):
    print(f'{brasileirao[c]}')

print(sorted(brasileirao))
posição = brasileirao.index('Flamengo')+1
print(f'O Flamengo está na {posição}ª posição')