#Ler o nome de uma pessoa mostrando o primero nome e o último
nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print('Primeiro nome: {}'.format(n[0]))
print('Último nome: {}'.format(n[len(n)-1]))