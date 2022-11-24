import pytest

from pytest import mark
from codigo.bytebank import Funcionario

class TestClass:
    def test_idade_recebe_14_10_1998_retorna_24(self):
        entrada = '14/10/1998' #Given - Esperado
        esperado = 24

        funcionario = Funcionario("Lucas", entrada, 3000)
        resultado = funcionario.idade() #When - Quando

        assert resultado == esperado #Then - Desfecho


    def test_nome_recebe_Lucas_Soares_retorna_Soares(self):
        entrada = "Lucas Soares"
        esperado = "Soares"

        lucas = Funcionario(entrada, "14/10/1998", 3000)
        resultado = lucas.sobrenome()

        assert resultado == esperado


    def test_quando_salario_recebe_100000_deve_retornar_90000(self):
        entrada_nome = "Felipe Leônidas"
        entrada_salario = 100000
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, "14/10/1998", entrada_salario)
        resultado = funcionario_teste.decrescimoSalario()

        assert resultado == esperado

    @mark.calcularBonus
    def test_quando_salario_recebe_1000_bonus_deve_retornar_100(self):
        entrada_nome = "Felipe Leônidas"
        entrada_salario = 1000
        esperado = 100

        funcionario_teste = Funcionario(entrada_nome, "14/10/1998", entrada_salario)
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

    @mark.calcularBonus
    def test_quando_salario_recebe_100000_bonus_deve_retornar_100(self):
        with pytest.raises(Exception):
            entrada_salario = 100000

            funcionario_teste = Funcionario('Teste', "14/10/1998", entrada_salario)
            resultado = funcionario_teste.calcular_bonus()

            assert resultado