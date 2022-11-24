#Ler o nome completo de uma pessoa e mostrar o nome em maíusculas, quantas letras e quantas letras tem o primeiro nome
nome = str(input('Digite seu nome completo: ')).strip()
print(nome)
print(nome.upper())
print(nome.lower())
print(len(nome)-nome.count(' '))
#print(nome.find(' '))
separa = nome.split()
print(len(separa[0]))