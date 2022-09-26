#Calcular aumento de 10% para salário superiores que R$1250,00 e 15% para inferiores
sal = float(input('Digite o seu salário para receber aumento: '))
if sal > 1250:
    print('Seu salário sofreu um aumento de R${} e passou a ser R${}'.format(sal*0.1,sal*1.1))
else:
    print('Seu salário sofreu um aumento de R${} e passou a ser R${}'.format(sal*0.15,sal*1.15))