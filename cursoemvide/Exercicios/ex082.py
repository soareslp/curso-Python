'''LER VÁRIOS NÚMEROS E COLOCAR EM UMA LISTA. DEPOIS CRIAR DUAS LISTAS UMA DE PARES E UMA DE ÍMPARES.
MOSTRAR AS TRÊS LISTAS QUE FORAM GERADAS'''
lista = []
listaImpar = []
listaPar = []
resp = ''
while True:
    atual = int(input('Digite um número: '))
    lista.append(atual)
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        listaPar.append(lista[c])
    else:
        listaImpar.append(lista[c])

print(lista)
print(listaPar)
print(listaImpar)