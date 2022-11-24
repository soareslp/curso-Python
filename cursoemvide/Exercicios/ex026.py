#Quantas vezes uma letra aparece, qual sua primeira posição e última posição
frase = str(input('Digite uma frase: ')).strip().upper()
print('A primeira letra {} aparece {} vezes na frase'.format(frase[0], frase.count('A')))
print('A primeira letra A aparece na posição: {}'.format(frase.find('A')+1))
print('A última letra A aparece na posição: {}'.format(frase.rfind('A')+1))