'''Aprovar o empréstimo para compra de uma casa.
O programa pergunta se o VALOR DA CASA, SALÁRIO e
QUANTOS ANOS vai pagar.
Calcule o valor da prestação mensal, sabendo que
ela não pode exceder 30% do salário ou então o
empréstimo será negado'''

casa = float(input('Qual o valor da casa a ser comprada? '))
salario = float(input('Qual o seu salário? '))
tempo = int(input('Quanto tempo em anos que você pretende pagar? '))

prestacao = (casa / (tempo * 12))

if prestacao > (salario * 0.3):
    print('O valor das prestações excede em 30% seu salário, EMPRÉSTIMO NEGADO!')
else:
    print('Emprestimo aceito!')