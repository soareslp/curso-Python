'''LER NOME, ANO DE NASCIMENTO E CARTEIRA DE TRABALHO E CADASTRE-OS
(COM IDADE) EM UM DICIONÁRIO SE POR ACASO A CTPS FOR DIFERENTE DE ZERO.
O DICIONÁRIO RECEBERÁ TAMBÉM O ANO DE CONTRATAÇÃO E O SALÁRIO.
CALCULE E ACRESCENTE, ALÉM DA IDADE, COM QUANTOS ANOS A
PESSOA VAI SE APOSENTAR'''
from datetime import datetime

pessoas = dict()
pessoas['nome'] = str(input('Nome: '))
nasc = int(input('Ano Nascimento: '))
pessoas['idade'] = (datetime.today().year - nasc)
carteira = int(input('Carteira de Trabalho (0 se não possui): '))
pessoas['ctps'] = carteira
if pessoas['ctps'] == 0:
    for k, v in pessoas.items():
        print(f'- {k} tem o valor {v}')
else:
    pessoas['contratação'] = int(input('Ano de Contratação: '))
    pessoas['salário'] = float(input('Salário: R$'))
    pessoas['aposentadoria'] = (pessoas['contratação'] + 35)
    for k, v in pessoas.items():
        print(f'- {k} tem o valor {v}')
