'''LER IDADE E SEXO DE CADA PESSOAS E PERGUNTAR SE QUER CONTINUAR, NO FINAL MOSTRAR:
QUANTAS PESSOAS TEM MAIS DE 18 ANOS
QUANTOS HOMENS
E QUANTAS MULHERES ABAIXO DE 20 ANOS'''

pausa = 'N'
contMaior = contHomens = contMulher = 0

while True:
    sexo = str(input('Digite seu sexo: ')).upper().strip()[0]
    idade = int(input('Digite sua idade: '))
    pausa = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if idade > 18:
        contMaior += 1
    if sexo in 'Mm':
        contHomens += 1
    if sexo in 'Ff' and idade < 20:
        contMulher += 1
    if pausa in 'Nn':
        break
print(f'\nFIM!\nForam contados:\n{contMaior} pessoas com mais de 18 anos\n{contHomens} homens\n{contMulher} mulheres '
      f'abaixo de 20 anos')
