nome = str(input('Digite seu nome: '))
if nome == 'Lucas':
    print('Seu nome é pica doidão!!!')
elif nome == 'Pedro' or nome =='Maria' or nome == 'João':
    print('Seu nome é bem comum no Brasil!')
elif nome in ('Ana Joana Brenda Carol Jéssica'):
    print('Seu nome feminino é de moça linda!')
else:
    print('Seu nome é comum')
print('Tenha um bom dia {}!'.format(nome))