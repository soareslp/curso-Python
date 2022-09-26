'''LER 5 VALORES NUMÉRICOS E GUARDAR EM UMA LISTA.
MOSTRAR O MAIOR E MENOR VALOR E SUAS POSIÇÕES'''
num = list()
for c in range(0, 5):
    num.append(int(input('Digite um número: ')))
print(f'O maior valor da lista é: {max(num)} e sua posição é: {num.index(max(num))+1}ª')
print(f'O menor valor da lista é: {min(num)} e sua posição é: {num.index(min(num))+1}ª')