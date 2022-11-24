'''Ano de nascimento de um jovem e informe de acordo com a idade:
se ainda vai ser alistar ao serviço militar
se é a hora de se alista
se passou da hora de se alistar
deve mostrar'''
import datetime
atual = datetime.date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc
print('Sua idade é: {}'.format(idade))
if idade < 18:
    idade = 18 - idade
    print('Ainda não é a hora de alistar, lhe faltam {} anos'.format(idade))
elif idade == 18:
    print('Parabéns se fodeu, chegou sua hora de alistar!')
elif idade > 18:
    idade = idade - 18
    print('O seu arrombado você passou {} anos sem se alistar, vai agora!'.format(idade))