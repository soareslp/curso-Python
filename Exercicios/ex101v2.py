'''CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA VOTO() QUE VAI RECEBER COMO PARÂMETRO
O ANO DE NASCIMENTO DE UMA PESSOAS, RETORNANDO UM VALOR LITERAL INDICANDO SE UMA PESSOA TEM VOTO
NEGADO, OPCIONAL OU OBRIGATÓRIO NAS ELEIÇÕES'''
def voto(ano):
    """
        -> Faz o retorno se o voto é obrigatório ou não dependendo da idade da pessoa
        :param nasc: Ano de nascimento da pessoa
        :return: Retornar o resultado se a pessoa é obrigada ou não a votar
        """
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 18:
        resp = str(f'Com {idade} anos, seu voto é: NÃO VOTA')
    elif idade <= 65:
        resp = str(f'Com {idade} anos, seu voto é: OBRIGATÓRIO')
    else:
        resp = str(f'Com {idade} anos, seu voto é: OPCIONAL')
    return resp


nasc = int(input('Em que ano você nasceu? '))
print(f'{voto(nasc)}')

