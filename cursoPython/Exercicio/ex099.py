'''FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA MAIOR(), QUE RECEBA VÁRIOS PARÂMETROS COM
VALORES INTEIROS. SEU PROGRAMA TEM QUE ANALISAR TODOS OS VALORES E DIZER QUAL DELES É O MAIOR'''


def maior(*num):
    mai = 0
    print('-=' * 25)
    print('Analisando os valores informados...')
    if len(num) == 0:
        print('Nenhuma valor informado...')
    for i in range(0, len(num)):
        print(f'{num[i]} ', end='')
        if i == 0:
            mai = num[0]
        if num[i] > mai:
            mai = num[i]
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor foi o {mai}.')
    print('-=' * 25)
    print()

maior(1, 6, 7, 3)
maior(2, 9)
maior(1)
maior()
