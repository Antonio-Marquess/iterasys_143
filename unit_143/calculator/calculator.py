def somar_dois_numeros(num1, num2):
    return num1 + num2

def subtrair_dois_numeros(num1, num2):
    return num1 - num2

def multiplicar_dois_numeros(num1, num2):
    return num1 * num2

def dividir_dois_numeros(num1, num2):
    try:
        return num1 / num2
    except(ZeroDivisionError):
        return 'Não é possível dividir por zero'

def area_do_triangulo(base, altura):
    """
    Calcula a área de um triângulo usando a fórmula:
    (base * altura) / 2
    """
    return (base * altura) / 2
