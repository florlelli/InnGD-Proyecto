import random #importamos la biblioteca random
from aritmetica import Aritmetica

class Captcha:
    def __init__(self):
        self.aritmetica = Aritmetica()

    def generar_captcha(self):
        opcion = ['sumar', 'restar', 'multiplicar', 'dividir']
        operacion = random.choice(opcion) #La función choice(secuencia) elige un valor al azar en un conjunto de elementos, en este caso, la lista opción.

        num1 = round(random.uniform(1, 10), 2)  #uniform() devuelve un num random flotante entre 1 y 10. El round es para que muestre solo dos decimales. 
        num2 = round(random.uniform(1, 10), 2)

        if operacion == 'sumar': #si el random elige "sumar" llamamos a la función sumar de la clase aritmetica
            resultado = self.aritmetica.sumar(num1, num2) #usamos los num randoms para la función y almacenamos en la variable resultado
            print(f"Resolver:\n{num1} + {num2} = ") #imprimmos el mensaje para que el usuario sepa que debe resolver esa operación generada. 
        elif operacion == 'restar':
            resultado = self.aritmetica.restar(num1, num2)
            print(f"Resolver:\n{num1} - {num2} = ")
        elif operacion == 'multiplicar':
            resultado = self.aritmetica.multiplicar(num1, num2)
            print(f"Resolver:\n{num1} * {num2} = ")
        elif operacion == 'dividir':
            resultado = self.aritmetica.dividir(num1, num2)
            print(f"Resolver:\n{num1} / {num2} = ")

        return resultado 