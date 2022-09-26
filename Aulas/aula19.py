pessoas = {'nome': 'Lucas', 'sexo': 'M', 'idade': 23}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)
print()
for k in pessoas.values():
    print(k)
print()
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()
#del pessoas['sexo']

pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print()
print(brasil[0])
print(brasil[1])
print(brasil)
print()
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

print()

estado = dict()
brasilzao = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasilzao.append(estado.copy())
for e in brasilzao:
    print(e)
print()
for e in brasilzao:
    for k, v in e.items():
        print(f'O campo {k} tem o ítem {v}')
print()
for e in brasilzao:
    for v in e.values():
        print(v, end=' ')
    print()
