def aumentar(v = 0, p = 0):
    res = v + (v * p/100)
    return res


def diminuir(v = 0, p = 0):
    res = v - (v * p / 100)
    return res


def dobro(v = 0):
    res = v * 2
    return res


def metade(v = 0):
    res = v / 2
    return res


def moeda(v= 0, moeda='R$'):
    v = str(f'{moeda}{v:.2f}'.replace('.',','))
    return v
