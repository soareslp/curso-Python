def aumentar(v = 0, p = 0, format=False):
    res = v + (v * p / 100)
    return res if format is False else moeda(res)


def diminuir(v = 0, p = 0, moedas = True):
    res = v - (v * p / 100)
    return res if format is False else moeda(res)


def dobro(v = 0, moedas = True):
    res = v * 2
    return res if format is False else moeda(res)


def metade(v = 0, moedas = True):
    res = v / 2
    return res if format is False else moeda(res)


def moeda(v= 0, moeda='R$'):
    v = str(f'{moeda}{v:.2f}'.replace('.',','))
    return v
