totMil = total = cont = menor = 0
nomeBarato = ''
while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totMil += 1
    if cont == 1 or preco < menor:
        menor = preco
        nomeBarato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'\nNo total foi gasto R${total:.2f}\n{totMil} produtos acima de R$1000,00\n{nomeBarato} foi o produto mais '
      f'barato custando R${menor:.2f}')
