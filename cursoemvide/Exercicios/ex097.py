'''FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA ESCREVA(), QUE RECEBA UM TEXTO
QULQUER COMO PARÂMETRO E MOSTRE UMA MENSAGEM COM TAMANHO ADAPTÁVEL.
EX: ESCREVA('OLÁ MUNDO!')
SAIDA: ~~~~~~~~~~
       OLÁ MUNDO
       ~~~~~~~~~~
'''
def escreva(txt):
    print('~' * len(txt))
    print(f'{txt}')
    print('~' * len(txt))


escreva('Lucas Soares')
escreva('PS4')
escreva('Final Fantasy VII')