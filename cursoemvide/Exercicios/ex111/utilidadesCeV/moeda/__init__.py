def aumentar(v = 0, p = 0, format=False):
    """
    -> Função responsável por acrescentar uma certa porcentagem a um valor estipulado, além de formatar o resultado
    :param v: Valor estipulado
    :param p: taxa de acréscimo
    :param format: booleano para se quer ou não a formatação
    :return: retorna o valor aumentado, com a opção de vir formatado ou não
    """
    res = v + (v * p / 100)
    return res if format is False else moeda(res)


def diminuir(v = 0, p = 0, moedas = True):
    """
        -> Função responsável por decrescentar uma certa porcentagem a um valor estipulado, além de formatar o resultado
        :param v: Valor estipulado
        :param p: taxa de decréscimo
        :param format: booleano para se quer ou não a formatação
        :return: retorna o valor aumentado, com a opção de vir formatado ou não
        """
    res = v - (v * p / 100)
    return res if format is False else moeda(res)


def dobro(v = 0, moedas = True):
    """
    -> Dobra um valor
    :param v: valor
    :param moedas: Opção de formatação
    :return: valor dobrado
    """
    res = v * 2
    return res if format is False else moeda(res)


def metade(v = 0, moedas = True):
    """
    -> Faz a metade de um valor
    :param v: valor
    :param moedas: Opção de formatação
    :return: valor dividido por 2
    """
    res = v / 2
    return res if format is False else moeda(res)


def moeda(v= 0, moeda='R$'):
    """
    -> Formata a moeda
    :param v: valor
    :param moeda: qual moeda
    :return: moeda formatada
    """
    v = str(f'{moeda}{v:.2f}'.replace('.',','))
    return v


def resumo(valor=0, aumento=0, redução=0):
    print('-' * 30)
    print('TABELA DE VALORES'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(valor, aumento, True)}')
    print(f'{redução}% de redução: \t{diminuir(valor, redução, True)}')
    print('-' * 30)
