#Saber seno, cosseno e tangente de um ângulo
'''import math

a = float(input("Digite um ângulo: "))
cos = math.cos(math.radians(a))
sin = math.sin(math.radians(a))
tan = math.tan(math.radians(a))

print("O ângulo {:.2f} apresenta:\nCosseno: {:.2f}\nSeno: {:.2f}\nTangente: {:.2f}".format(a, cos, sin, tan))'''


from math import radians, sin, cos, tan

a = float(input("Digite um ângulo: "))
cos = cos(radians(a))
sin = sin(radians(a))
tan = tan(radians(a))

print("O ângulo {:.2f} apresenta:\nCosseno: {:.2f}\nSeno: {:.2f}\nTangente: {:.2f}".format(a, cos, sin, tan))