import pytest
from calculadora import Calculadora


@pytest.fixture
def calc():
    return Calculadora()

# Teste de soma
def test_somar(calc):
    assert calc.somar(7, 32) == 39
    assert calc.somar(80, 60) == 140

# Teste de subtração
def test_subtrair(calc):
    assert calc.subtrair(64, 5) == 59
    assert calc.subtrair(70, 20) == 50

# Teste de multiplicação
def test_multiplicar(calc):
    assert calc.multiplicar(50, 3) == 150
    assert calc.multiplicar(60, 2) == 120

# Teste de divisão
def test_dividir(calc):
    assert calc.dividir(8, 2) == 4

# Teste de exceção para divisão por zero
def test_dividir_por_zero(calc):
    with pytest.raises(ValueError, match="Divisão por zero não é permitida."):
        calc.dividir(50, 0)