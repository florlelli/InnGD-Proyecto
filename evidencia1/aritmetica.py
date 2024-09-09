class Aritmetica:

    def sumar(self, num1 : float, num2 : float):
        return round(num1 + num2, 2)

    def restar(self, num1 : float, num2 : float):
        return round(num1 - num2, 2)

    def dividir(self, num1 : float, num2 : float):
        try:
            return round(num1 / num2, 2)
        except ZeroDivisionError:
            return None

    def multiplicar(self, num1 : float, num2 : float):
        return round(num1 * num2, 2)

    def sumar_n(self, lista : float): #lista va a representar una lista para el módulo de asersiones
        return round(sum(lista), 2)

    def promedio_n(self, lista): #lo mismo acá
        return round(sum(lista) / len(lista), 2)