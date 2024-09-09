# Modulo aritmetica

def sumar(a: float, b: float) -> float:
    """Suma de dos números"""
    return round(a + b, 2)

def restar(a: float, b: float) -> float:
    """Resta de dos números"""
    return round(a - b, 2)

def dividir(a: float, b: float) -> float:
    """División de dos números"""
    try:
        assert b != 0, "Error: No se puede dividir por cero."
        return round(a / b, 2)
    except AssertionError as e:
        return str(e)

def multiplicar(a: float, b: float) -> float:
    """Multiplicación."""
    return round(a * b, 2)

def sumar_n(*numeros: float) -> float:
    """Suma de n números"""
    return round(sum(numeros), 2)

def promedio_n(*numeros: float) -> float:
    """Promedio de n números"""
    try:
        assert len(numeros) > 0, "Error: No se puede calcular el promedio de 0 números."
        return round(sum(numeros) / len(numeros), 2)
    except AssertionError as e:
        return str(e)
