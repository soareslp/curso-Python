'''DIGITAR UMA EXPRESSÃO QUE USE PARÊNTESES. O APLICATIVO DEVE VER SE A EXPRESSÃO PASSADA ESTÁ COM OS
PARÊNTESES ABERTOS E FECHADOS NA ORDEM CORRETA'''
lista = []
contI = 0
contF = 0

expressão = str(input('Digite sua expressão: '))
for simb in expressão:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')

