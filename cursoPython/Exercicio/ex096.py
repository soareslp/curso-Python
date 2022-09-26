'''FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA ÁREA(), QUE RECEBA AS DIMENSÕES
DE UM TERRENO RETANGULAR (LARGURA E COMPRIMENTO) E MOSTRE A ÁREA DO TERRENO.'''
def área():
    print('CONTROLE DE TERRENOS')
    print('--------------------')
    larg = float(input('LARGURA (m): '))
    compr = float(input('COMPRIMENTO (m): '))
    s = larg * compr
    print(f'A área de um terreno de {larg} x {compr} é de {s}m²')
área()