'''ADAPTE O CÓDIGO DO DESAFIO 107, CRIANDO UMA FUNÇÃO ADICIONAL CHAMADA MOEDA()
QUE CONSIGA MOSTRAR OS VALORES COMO UM VALOR MONETÁRIO FORMATADO.'''
from ex108 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é: {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é: {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando {moeda.moeda(p)} em 10%, temos: {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Reduzindo {moeda.moeda(p)} em 13%, temos: {moeda.moeda(moeda.diminuir(p, 13))}')