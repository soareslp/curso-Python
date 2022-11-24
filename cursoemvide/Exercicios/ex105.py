'''FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO NOTAS() QUE PODE RECEBER VÁRIAS NOTAS DE ALUNOS
E VAI RETORNAR UM DICIONÁRIO COM AS SEGUINTES INFORMAÇÕES:
- QUANTIDADE DE NOTAS
- A MAIOR NOTA
- A MENOR NOTA
- A MÉDIA DA TURMA
- A SITUAÇÃO (OPCIONAL)
ADICIONE TAMBÉM AS DOCSTRINGS DA FUNÇÃO'''


def notas(*num, sit=False):
    lista = dict()
    soma = media = maior = menor = 0
    lista['total'] = len(num)
    for n in range(0, len(num)):
        if num[0]:
            maior = menor = num[0]
        if num[n] > maior:
            maior = num[n]
        if num[n] < menor:
            menor = num[n]
        soma += num[n]
    media = soma / len(num)
    lista['maior'] = maior
    lista['menor'] = menor
    lista['media'] = media
    if sit:
        if media < 4:
            lista['situação'] = 'PÉSSIMA'
        if 4 <= media <= 6:
            lista['sutuação'] = 'RUIM'
        if media > 6:
            lista['sutuação'] = 'BOA'
    return lista

resp = notas(5.5, 10, 5, sit=True)
print(resp)
