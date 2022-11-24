from datetime import date

class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
        nascimento_partido = self._data_nascimento.split('/')
        ano_nascimento = nascimento_partido[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)

    def sobrenome(self):
        nome_completo = self._nome.strip()
        nome_partido = nome_completo.split(' ')
        return nome_partido[-1]

    def _ehSocio(self):
        sobrenomes = ['Bragança', 'Leônidas', 'Andrade', 'Silveira', 'Castro']
        return self._salario >= 100000 and (self.sobrenome() in sobrenomes)

    def decrescimoSalario(self):
        if self._ehSocio():
            decrescimo = (self._salario * 0.9)
        return decrescimo

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception("O salário é muito alto para receber o bônus")
        return valor

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})';