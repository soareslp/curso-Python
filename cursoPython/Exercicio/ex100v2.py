'''FAÇA UM PROGRAMA QUE TENHA UMA LISTA CHAMADA NÚMEROS E DUAS FUNÇÕES CHAMADAS SORTEIO() E SOMAPAR().
A PRIMEIRA FUNÇÃO VAI SORTEAR 5 NÚMEROS E VAI COLOCÁ-LOS DENTRO DA LISTA E A SEGUNDA FUNÇÃO VAI MOSTRAR
A SOMA ENTRE TODOS OS VALORES PARES SORTEADOS PELA FUNÇÃO ANTERIOR'''
from random import randint

list = []
def sorteio():
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        list.append(randint(1, 10))
        print(f'{list[c]}', end=' ')

def somaPar():
    soma = 0
    print(f'\nSomando os valores pares da lista {list} temos: ', end='')
    for c in range(0, len(list)):
        if list[c] % 2 == 0:
            soma += list[c]
    print(soma)