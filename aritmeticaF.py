def sumar(a, b):
    return round(a + b, 2)

def restar(a, b):
    return round(a - b, 2)

def multiplicar(a, b):
    return round(a * b, 2)

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return round(a / b, 2)

def sumar_n(*args):
    return round(sum(args), 2)

def promedio_n(*args):
    return round(sum(args) / len(args), 2)
