'''FAZER O USUÁRIO DIGITAR NÚMEROS ATÉ QUE DIGITE 999, MOSTRAR ELES E NO FIM SUA SOMA TAMBÉM'''

soma = cont = 0
n = int(input('Digite um número [999 para parar]:'))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [999 para parar]:'))
print('A SOMA dos {} números digitados foi: {}'.format(cont, soma))