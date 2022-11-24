lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
#Tuplas são imutáveis
#lanche[1] = 'Refrigerante'
print(lanche)
print(len(lanche))
print(lanche[1])
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
print(lanche[-3:])

for comida in lanche:
    print(f'Vou comer {comida}')
print('\nComi muito! Tava cagado de fome\n')

for cont in range(0, len(lanche)):
    print(f'Vou comer {lanche[cont]} na posição {cont}')
print('\nComi muito! Tava cagado de fome\n')

for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} na pos {pos}')
print('Comi muito! Tava cagado de fome\n')

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1,2)
print(a)
print(b)
c = a + b
print(c)
print(len(c))
print(c.count(5))
print(c.count(4))
print(c.count(9))
print(c)
print(c.index(8))
print(c.index(2))
print(c.index(2, 1))

pessoa = ('Lucas', 23, 'M', 55.60)
del(pessoa)
print(pessoa)
