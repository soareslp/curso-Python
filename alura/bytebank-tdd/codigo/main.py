from codigo.bytebank import Funcionario

#lucas = Funcionario("Lucas", "14/10/1998", 1000)

#print(lucas.idade())

def teste_idade():
    lucas_teste = Funcionario('Lucas', "14/10/1998", 2300)
    print(f'Teste = {lucas_teste.idade()}')

teste_idade()