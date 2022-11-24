'''CRIE UM MÓDULO CHAMADO MOEDA.PY QUE TENHA AS FUNÇÕES INCORPORADAS AUMENTAR(),
DIMINUIR(), DOBRO() E METADE().
FAÇA TAMBÉM UM PROGRAMA QUE IMPORTE ESSE MÓDULO E USE ALGUMAS DESSAS FUNÇÕES'''
from ex107 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é: {moeda.metade(p)}')
print(f'O dobro de {p} é: {moeda.dobro(p)}')
print(f'Aumentando {p} em 10%, temos: {moeda.aumentar(p, 10)}')
print(f'Reduzindo {p} em 13%, temos: {moeda.diminuir(p, 13)}')