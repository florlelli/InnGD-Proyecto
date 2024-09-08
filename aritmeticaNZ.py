# aritmeticaNZ.py

import re

def sumar(a: float, b: float) -> float:
    """Suma dos números reales y devuelve la suma."""
    assert isinstance(a, (int, float)) and isinstance(b, (int, float)), "Ambos argumentos deben ser números"
    return round(a + b, 2)

def restar(a: float, b: float) -> float:
    """Resta el segundo número del primero y devuelve el resultado."""
    assert isinstance(a, (int, float)) and isinstance(b, (int, float)), "Ambos argumentos deben ser números"
    return round(a - b, 2)

def dividir(a: float, b: float) -> float:
    """Divide el primer número por el segundo y devuelve el resultado.
    Maneja la excepción de división por cero.
    """
    assert isinstance(a, (int, float)) and isinstance(b, (int, float)), "Ambos argumentos deben ser números"
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return round(a / b, 2)

def multiplicar(a: float, b: float) -> float:
    """Multiplica dos números reales y devuelve el resultado."""
    assert isinstance(a, (int, float)) and isinstance(b, (int, float)), "Ambos argumentos deben ser números"
    return round(a * b, 2)

def sumar_n(*args: float) -> float:
    """Suma una cantidad variable de números reales y devuelve la suma."""
    if not all(isinstance(x, (int, float)) for x in args):
        raise ValueError("Todos los argumentos deben ser números")
    return round(sum(args), 2)

def promedio_n(*args: float) -> float:
    """Calcula el promedio de una cantidad variable de números reales y devuelve el resultado."""
    if not args:
        raise ValueError("Debe proporcionar al menos un número para calcular el promedio")
    if not all(isinstance(x, (int, float)) for x in args):
        raise ValueError("Todos los argumentos deben ser números")
    return round(sum(args) / len(args), 2)