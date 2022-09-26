teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)


galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])
for p in galera:
    print(p)

for p in galera:
    print(p[0])

for p in galera:
    print(p[1])

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

galerinha = list()
dado = list()
totMai = totMen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(str(input('Idade: ')))
    galerinha.append(dado[:])
    dado.clear()
print(galerinha)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totMai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totMen += 1
print(f'Temos {totMai} maiores e {totMen} menores de idade')
