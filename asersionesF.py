import aritmetica

def test_sumar():
    assert aritmetica.sumar(2.5, 3.5) == 6.00
    assert aritmetica.sumar(1, 1) == 2.00
    assert aritmetica.sumar(-1, 5) == 4.00

def test_restar():
    assert aritmetica.restar(5, 2) == 3.00
    assert aritmetica.restar(5, 5) == 0.00
    assert aritmetica.restar(-1, -1) == 0.00

if __name__ == "__main__":
    test_sumar()
    test_restar()
