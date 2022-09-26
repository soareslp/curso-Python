'''FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA ÁREA(), QUE RECEBA AS DIMENSÕES
DE UM TERRENO RETANGULAR (LARGURA E COMPRIMENTO) E MOSTRE A ÁREA DO TERRENO.'''
def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno de {larg} x {comp} é de {a}m²')


print('CONTROLE DE TERRENOS')
print('--------------------')
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)