import random
import aritmetica

def generar_captcha():
    a = random.uniform(1, 10)
    b = random.uniform(1, 10)
    resultado_correcto = aritmetica.sumar(a, b)
    print(f"Captcha: {a:.2f} + {b:.2f} = ?")
    respuesta = float(input("Ingrese el resultado: "))

    if round(respuesta, 2) == resultado_correcto:
        print("Captcha correcto")
        return True
    else:
        print("Captcha incorrecto")
        return False
