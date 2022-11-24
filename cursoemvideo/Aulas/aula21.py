def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela
    :param a:o primeiro valor (opcional)
    :param b:o segundo valor (opcional)
    :param c:o terceiro valor (opcional)
    Função criada por Lucas Soares do Canal 2 Player
    """
    s = a + b + c
    print(f'A soma vale {s}')

def somarReturn(a=0, b=0, c=0):
    s = a + b + c
    return s


somar(3, 2, 5)
somar(3, 3)

r1 = somarReturn(3, 2, 5)
r2 = somarReturn(1, 7)
r3 = somarReturn(4)
print(f'Somas valem {r1}, {r2} e {r3}')