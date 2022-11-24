'''Calcular o preço do produto com o preço normal e condição de pagamento
À vista dinheiro/cheque: 10% de desconto
No cartão à vista: 5% desconto
2x no cartão: preço normal
3x ou mais: 20% juros'''

valor = float(input('Qual o valor total da compra? '))
opc = int(input('Qual vai ser a sua opção de pagamento?\n[1]À vista no dinheiro ou cheque\n[2]Cartão à vista\n'
                '[3]Cartão 2x\n[4]Cartão 3x ou mais\nQual sua opção?'))
if opc == 1:
    print('A sua compra de R${:.2f} ganha um desconto de 10% e passa a ser R${:.2f}'.format(valor, valor*0.9))
elif opc == 2:
    print('A sua compra de R${:.2f} ganha um desconto de 5% e passa a ser R${:.2f}'.format(valor, valor*0.95))
elif opc == 3:
    print('A sua compra de R${:.2f} não ganha desconto'.format(valor))
elif opc == 4:
    print('A sua compra de R${:.2f} sofre juros de 20% e passa a ser R${:.2f}'.format(valor,valor*1.2))
