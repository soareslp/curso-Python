'''PEGAR VÁRIOS VALORES NUMÉRICOS E JOGAR NUMA LISTA, SE JÁ EXISTIR NÃO COLOCAR.
MOSTRAR OS VALORES DA LISTA EM ORDEM CRESCENTE'''
num = list()
resp = ''
while True:
    atual = int(input('Digite um valor: '))
    if atual not in num:
        num.append(atual)
        print('Adicionado com sucesso!')
    else:
        print('Não vou adicionar, valor duplicado!')
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'Nn':
        break
num.sort()
print(f'A sua lista é: {num}')
