nome = str(input('Qual é o seu nome: '))
if nome == 'Lucas':
    print('Seu nome é tão belo!')
else:
    print('Seu nome é uma merda!')
print('Bom dia, {}!'.format(nome))

#-------------------------------------------------------------#

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
if media>=6:
    print("A sua média foi {:.1f}, PARABÉNS!".format(media))
else:
    print("A sua média foi {:.1f}, ESTUDE MAIS SEU BURRO!".format(media))