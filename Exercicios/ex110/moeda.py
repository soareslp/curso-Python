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
    resp = str(f'{"-" * 30}\n'
               f'{"TABELA DE VALORES":^30}'
               f'\n{"-" * 30}'
               f'\nPreço analisado: {moeda(valor):>15}'
               f'\nDobro do preço: {dobro(valor, True):>17}'
               f'\nMetade do preço: {metade(valor, True):>15}'
               f'\n{aumento}% de aumento: {aumentar(valor, aumento, True):>17}'
               f'\n{redução}% de redução: {diminuir(valor, redução, True):>16}')
    return print(resp)
