from aritmetica import Aritmetica

def test_sumar():
    usar = Aritmetica() #instanciamos la clase Aritmetica
    assert usar.sumar(2.25, 2.25) == 4.50, "Error. "
    assert usar.sumar(7, 7) == 14, "Error. "
    assert usar.sumar(75.34, 82.15) == 157.49, "Error. "

def test_restar():
    usar = Aritmetica()
    assert usar.restar(12.47, 5.32) == 7.15, "Error. "
    assert usar.restar(16.20, 1.20) == 15.0, "Error. "
    assert usar.restar(9.63, 4.52) == 5.11, "Error. "

def test_dividir():
    usar = Aritmetica()
    assert usar.dividir(25.98, 4.14) == 6.28, "Error. "
    assert usar.dividir(16, 4) == 4, "Error. "
    assert usar.dividir(20, 0) is None, "No se puede dividir entre 0.\n"

def test_multiplicar():
    usar = Aritmetica()
    assert usar.multiplicar(7.14, 10) == 71.4, "Error. "
    assert usar.multiplicar(2, 8) == 16, "Error. "
    assert usar.multiplicar(1, 4) == 4, "Error. "

def test_sumar_n():
    usar = Aritmetica()
    assert usar.sumar_n([1, 1, 10]) == 12, "Error. "
    assert usar.sumar_n([12.47, 2.325, 5.1]) == 19.89, "Error. "
    assert usar.sumar_n([0, 1]) == 1, "Error. "

def test_promedio_n():
    usar = Aritmetica()
    assert usar.promedio_n([1, 1, 10]) == 4, "Error. "
    assert usar.promedio_n([12.47, 2.325, 5.1]) == 6.63, "Error. "
    assert usar.promedio_n([2, 2]) == 2, "Error. "

if __name__ == "__main__":
    test_sumar()
    test_restar()
    test_dividir()
    test_multiplicar()
    test_sumar_n()
    test_promedio_n()
    print("Pruebas terminadas.")