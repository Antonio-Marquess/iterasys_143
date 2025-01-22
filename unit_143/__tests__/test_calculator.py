import pytest

from calculator.calculator import somar_dois_numeros,       \
                                    subtrair_dois_numeros,    \
                                    multiplicar_dois_numeros, \
                                    dividir_dois_numeros,     \
                                    area_do_triangulo

from utils.utils import ler_csv

def test_somar_dois_numeros():
    # AAA  

    # Arrange - Configura
    num1 = 5
    num2 = 7
    resultado_esperado = 12

    # Act - Executa
    resultado_atual = somar_dois_numeros(num1, num2)

    # Assert - Valida
    assert resultado_esperado == resultado_atual

def test_subtrair_dois_numeros():
    # AAA

    # Arrange - Configura
    num1 = 5
    num2 = 7
    resultado_esperado = -2

    # Act - Executa
    resultado_atual = subtrair_dois_numeros(num1, num2)

    # Assert - Valida
    assert resultado_esperado == resultado_atual

def test_multiplicar_dois_numeros():
    # AAA

    # Arrange - Configura
    num1 = 5
    num2 = 7
    resultado_esperado = 35

    # Act - Executa
    resultado_atual = multiplicar_dois_numeros(num1, num2)

    # Assert - Valida
    assert resultado_esperado == resultado_atual

def test_dividir_dois_numeros():
    # AAA

    # Arrange - Configura
    num1 = 12
    num2 = 3
    resultado_esperado = 4

    # Act - Executa
    resultado_atual = dividir_dois_numeros(num1, num2)

    # Assert - Valida
    assert resultado_esperado == resultado_atual
    

def test_dividir_por_zero():
    # AAA

    # Arrange - Configura
    num1 = 12
    num2 = 0
    resultado_esperado = 'Não é possível dividir por zero'

    # Act - Executa
    resultado_atual = dividir_dois_numeros(num1, num2)

    # Assert - Valida
    assert resultado_esperado == resultado_atual

@pytest.mark.parametrize('num1, num2, resultado_esperado',[
    (5,7,12), #tupla
    (3,0,3),
    (-1,6,5),
    (-9,-2,-11),
    (0.5,0.25,0.75)
])
def test_somar_dois_numeros_lista(num1, num2, resultado_esperado):
    # AAA

    # Arrange - Configura
    # Dados vêm da lista acima (parametrize)

    # Act - Executa
    resultado_atual = somar_dois_numeros(num1, num2)

    # Assert - Valida
    assert resultado_esperado == resultado_atual

@pytest.mark.parametrize('num1, num2, resultado_esperado',
      ler_csv('./fixtures/csv/massa_somar.csv')                   
)
def test_somar_dois_numeros_csv(num1, num2, resultado_esperado):
    # AAA

    # Arrange - Configura
    # Dados vêm do parametrize acima

    # Act - Executa
    resultado_atual = somar_dois_numeros(float(num1), float(num2))

    # Assert - Valida
    assert float(resultado_esperado) == resultado_atual


@pytest.mark.parametrize('id, op, num1, num2, resultado_esperado',[
    (1,'Soma',5,7,12), #tupla
    (2,'Sub',3,1,2),
    (3,'Mult',-1,6,-6),
    (4,'Div',-9,-2,4.5),
    (5,'Div', 6,0,'Não é possível dividir por zero')
])
def test_calcular_dois_numeros_lista(id, op, num1, num2, resultado_esperado):
    # AAA

    # Arrange - Configura
    # Dados vêm da lista acima (parametrize)
    resultado_atual = ''
    # Act - Executa
    match(op):
        case "Soma":
            resultado_atual = somar_dois_numeros(num1, num2)
        case "Sub":
            resultado_atual = subtrair_dois_numeros(num1, num2)
        case "Mult":
            resultado_atual = multiplicar_dois_numeros(num1, num2)
        case "Div":
            resultado_atual = dividir_dois_numeros(num1, num2)
        case _:
            print("valor inesperado de operação")

    # Assert - Valida
    assert resultado_esperado == resultado_atual

@pytest.mark.parametrize('base, altura, resultado_esperado', [
    (10, 5, 25),   # Teste 1: base = 10, altura = 5
    (8, 4, 16),    # Teste 2: base = 8, altura = 4
])
def test_area_do_triangulo(base, altura, resultado_esperado):
    # AAA

    # Arrange - Configura
    # Dados vêm do parametrize acima

    # Act - Executa
    resultado_atual = area_do_triangulo(base, altura)

    # Assert - Valida
    assert resultado_esperado == resultado_atual
