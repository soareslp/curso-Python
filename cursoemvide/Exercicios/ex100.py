'''FAÇA UM PROGRAMA QUE TENHA UMA LISTA CHAMADA NÚMEROS E DUAS FUNÇÕES CHAMADAS SORTEIO() E SOMAPAR().
A PRIMEIRA FUNÇÃO VAI SORTEAR 5 NÚMEROS E VAI COLOCÁ-LOS DENTRO DA LISTA E A SEGUNDA FUNÇÃO VAI MOSTRAR
A SOMA ENTRE TODOS OS VALORES PARES SORTEADOS PELA FUNÇÃO ANTERIOR'''
from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ')
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    print(f'\nSomando os valores pares da lista {lista} temos: ', end='')
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(soma)

numeros = list()
sorteia(numeros)
somaPar(numeros)