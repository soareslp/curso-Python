'''Tupla com várias palavras sem acentos e mostrar quais as vogais nas palavras'''
palavras = ('jogar', 'escutar', 'musica', 'comedia', 'filme', 'caçador', 'avenida', 'esquina', 'engenheiro')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')