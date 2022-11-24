km = float(input("Quantos km o carro rodou?"))
d = float(input("Por quantos dias o carro foi alugado?"))
a = (60 * d) + (0.15 * km);
print("Aluguel custa R${:.2f}!".format(a));