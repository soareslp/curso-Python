print('\033[0;30;41mOlá Mundo!\033[m')
print('\033[1;31;42mOlá Mundo!\033[m')
print('\033[4;32;43mOlá Mundo!\033[m')
print('\033[7;33;44mOlá Mundo!\033[m')
print('\033[7;30mOlá Mundo!\033[m')

a = 5
b = 3
print('Os valores são \033[32m{}\033[m e \033[35m{}'.format(a, b))

nome = 'Lucas'
print('Olá prazer em te conhecer {}{}{}'.format('\033[32m',nome,'\033[m'))