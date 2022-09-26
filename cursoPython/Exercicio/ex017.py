import math

'''co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = (co ** 2 + ca ** 2) ** (1/2)
print("Hipotenusa é: {:.2f}".format(hi))'''

co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = math.hypot(ca, co)
print("Hipotenusa é: {:.2f}".format(hi))