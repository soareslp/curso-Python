'''LER NOME E PREÇO DE UM PRODUTO. PERGUNTAR SE VAI CONTINUAR E MOSTRAR:
 GASTO TOTAL
 QUANTOS PRODUTOS MAIS DE R$1000
 NOME DO PRODUTO MAIS BARATO'''

contMil = total = 0
precoBarato = 999999
nomeBarato = ''
total = 0
pausa = 'Ss'

while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    total += preco
    pausa = str(input('\nQuer continuar? [S/N]'))
    if preco > 1000:
        contMil += 1
    if preco < precoBarato:
        precoBarato = preco
        nomeBarato = nome
    if pausa in 'Nn':
        break
print(f'\nNo total foi gasto R${total:.2f}\n{contMil} produtos acima de R$1000,00\n{nomeBarato} foi o produto mais '
      f'barato custando R${precoBarato}')
