import aritmetica

def test_sumar():
    assert aritmetica.sumar(5.0, 3.0) == 8.0
    assert aritmetica.sumar(-1.5, 2.0) == 0.5
    assert aritmetica.sumar(1.12345, 1.87655) == 3.0

def test_restar():
    assert aritmetica.restar(10.0, 5.0) == 5.0
    assert aritmetica.restar(-3.5, -1.5) == -2.0
    assert aritmetica.restar(5.55, 0.55) == 5.0

def test_dividir():
    assert aritmetica.dividir(10.0, 2.0) == 5.0
    assert aritmetica.dividir(9.0, 3.0) == 3.0
    assert aritmetica.dividir(5.0, 0.0) == "Error: No se puede dividir por cero."

def test_multiplicar():
    assert aritmetica.multiplicar(3.0, 2.0) == 6.0
    assert aritmetica.multiplicar(-1.5, 4.0) == -6.0
    assert aritmetica.multiplicar(2.5, 1.2) == 3.0

def test_sumar_n():
    assert aritmetica.sumar_n(1.0, 2.0, 3.0) == 6.0
    assert aritmetica.sumar_n(1.1, 2.2, 3.3, 4.4) == 11.0
    assert aritmetica.sumar_n() == 0.0

def test_promedio_n():
    assert aritmetica.promedio_n(1.0, 2.0, 3.0) == 2.0
    assert aritmetica.promedio_n(4.0, 6.0) == 5.0
    assert aritmetica.promedio_n() == "Error: No se puede calcular el promedio de 0 números."

# Ejecución de los tests
if __name__ == "__main__":
    test_sumar()
    test_restar()
    test_dividir()
    test_multiplicar()
    test_sumar_n()
    test_promedio_n()
    print("Todos los tests pasaron correctamente.")
