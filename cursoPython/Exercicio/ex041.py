'''ler o ano de nascimento e de acordo com a idade falar a categoria:
Até 9 anos: Mirim
Até 14 anos: Infantil
Até 19 anos: Junior
Até 20 anos: Sênior
Acima: Master'''
import datetime

nasc = int(input('Digite seu ano de nascimento: '))
idade = datetime.date.today().year - nasc
if idade <= 9:
    print('Por possuir {} anos, sua categoria é: \033[33m{}\033[m'.format(idade, 'Mirim'))
elif idade <=14:
    print('Por possuir {} anos, sua categoria é: \033[34m{}\033[m'.format(idade, 'Infantil'))
elif idade <= 19:
    print('Por possuir {} anos, sua categoria é: \033[35m{}\033[m'.format(idade, 'Junior'))
elif idade <= 20:
    print('Por possuir {} anos, sua categoria é: \033[36m{}\033[m'.format(idade, 'Sênior'))
else:
    print('Por possuir {} anos, sua categoria é: \033[32m{}\033[m'.format(idade, 'Master'))