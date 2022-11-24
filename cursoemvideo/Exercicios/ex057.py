'''LER O SEXO DA PESSOA QUE SÓ ACEITE 'M' OU 'F' COMO VALOR CERTO, SE FOR DIFERENTE FAÇA DE NOVO'''

sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dado inválido. Digite seu sexo novamente [M/F]: ')).upper().strip()[0]
print('Seu sexo é {}'.format(sexo))
