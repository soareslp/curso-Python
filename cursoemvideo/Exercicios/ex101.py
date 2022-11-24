'''CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA VOTO() QUE VAI RECEBER COMO PARÂMETRO
O ANO DE NASCIMENTO DE UMA PESSOAS, RETORNANDO UM VALOR LITERAL INDICANDO SE UMA PESSOA TEM VOTO
NEGADO, OPCIONAL OU OBRIGATÓRIO NAS ELEIÇÕES'''
from datetime import date


def voto(nasc):
    """
        -> Faz o retorno se o voto é obrigatório ou não dependendo da idade da pessoa
        :param nasc: Ano de nascimento da pessoa
        :return: Retornar o resultado se a pessoa é obrigada ou não a votar
        """
    resp = ''
    idade = date.today().year - nasc
    if idade < 18:
        resp = str(f'Com {idade} anos, seu voto é: NÃO OBRIGATÓRIO')
    elif idade <= 65:
        resp = str(f'Com {idade} anos, seu voto é: OBRIGATÓRIO')
    else:
        resp = str(f'Com {idade} anos, seu voto é: OPCIONAL')
    return resp


ano = int(input('Em que ano você nasceu? '))
v1 = voto(ano)
print(f'{v1}')
