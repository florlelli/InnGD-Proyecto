import re
from datetime import datetime
import random
import aritmetica 

usuarios = {}


def validar_nombre_usuario(nombre_usuario):
    return 6 <= len(nombre_usuario) <= 12


def validar_contrasena(contrasena):
    if len(contrasena) < 8:
        return False
    
    tiene_minuscula = re.search(r'[a-z]', contrasena) is not None
    tiene_mayuscula = re.search(r'[A-Z]', contrasena) is not None
    tiene_numero = re.search(r'[0-9]', contrasena) is not None
    tiene_especial = re.search(r'[\W_]', contrasena) is not None

    condiciones_cumplidas = sum([tiene_minuscula, tiene_mayuscula, tiene_numero, tiene_especial])
    return condiciones_cumplidas >= 2


def generar_captcha():
    operaciones = [aritmetica.sumar, aritmetica.restar, aritmetica.multiplicar, aritmetica.dividir]
    a = round(random.uniform(1, 100), 2)
    b = round(random.uniform(1, 100), 2)
    operacion = random.choice(operaciones)

    if operacion == aritmetica.dividir and b == 0:
        b = round(random.uniform(1, 100), 2)  

    if operacion == aritmetica.sumar:
        print(f"Resuelve la siguiente operación: {a} + {b}")
    elif operacion == aritmetica.restar:
        print(f"Resuelve la siguiente operación: {a} - {b}")
    elif operacion == aritmetica.multiplicar:
        print(f"Resuelve la siguiente operación: {a} * {b}")
    elif operacion == aritmetica.dividir:
        print(f"Resuelve la siguiente operación: {a} / {b}")
    
    return round(operacion(a, b), 2)


def verificar_captcha():
    while True:
        resultado_correcto = generar_captcha()
        respuesta_usuario = input("Ingresa el resultado con dos decimales: ")

        try:
            respuesta_usuario = float(respuesta_usuario)
            if round(respuesta_usuario, 2) == resultado_correcto:
                print("¡CAPTCHA correcto! Continuando con el registro.")
                return True
            else:
                print("Respuesta incorrecta.")
        except ValueError:
            print("Debe ingresar un número válido.")
        
        opcion = input("¿Deseas intentar otro CAPTCHA? (s/n): ").lower()
        if opcion == 'n':
            print("Saliendo del registro.")
            return False

def registrar_usuario():
    try:
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        dni = input("Ingrese su DNI: ")
        correo = input("Ingrese su correo electrónico: ")
        fecha_nacimiento = input("Ingrese su fecha de nacimiento (DD/MM/YYYY): ")

        
        try:
            datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Formato de fecha incorrecto, debe ser DD/MM/YYYY.")
        
       
        if dni in [usuario['dni'] for usuario in usuarios.values()]:
            raise ValueError("El DNI ya está registrado.")
        
        nombre_usuario = input("Ingrese un nombre de usuario (6-12 caracteres): ")
        if not validar_nombre_usuario(nombre_usuario):
            raise ValueError("El nombre de usuario debe tener entre 6 y 12 caracteres.")
        
        
        if nombre_usuario in usuarios:
            raise ValueError("El nombre de usuario ya está registrado.")
        
        contrasena = input("Ingrese una contraseña: ")
        if not validar_contrasena(contrasena):
            raise ValueError("La contraseña debe tener al menos 8 caracteres y cumplir con al menos 2 de las condiciones: minúscula, mayúscula, número o carácter especial.")

        
        print("Para completar el registro, resuelve el siguiente CAPTCHA:")
        if not verificar_captcha():
            print("Registro cancelado.")
            return

        
        usuarios[nombre_usuario] = {
            'nombre': nombre,
            'apellido': apellido,
            'dni': dni,
            'correo': correo,
            'fecha_nacimiento': fecha_nacimiento,
            'clave': contrasena
        }
        
        print(f"¡Usuario {nombre_usuario} registrado exitosamente!")
    
    except ValueError as e:
        print(f"Error: {e}")


def mostrar_usuarios():
    if usuarios:
        print("\nUsuarios registrados:")
        for username, info in usuarios.items():
            print(f"Usuario: {username}, Nombre completo: {info['nombre']} {info['apellido']}, DNI: {info['dni']}")
    else:
        print("No hay usuarios registrados.")



def menu():
    while True:
        print("\n1. Registrar usuario")
        print("2. Mostrar usuarios registrados")
        print("3. Salir")
        
        opcion = input("Elija una opción: ")
        
        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            mostrar_usuarios()
        elif opcion == '3':
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == '__main__':
    menu()
