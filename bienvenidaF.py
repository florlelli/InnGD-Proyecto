import re

usuarios = {}

def bienvenida():
    print("Bienvenido a la aplicación de gestión")
    opcion = input("1. Ingresar \n2. Registrar \nSeleccione una opción: ")
    
    if opcion == "2":
        registrar_usuario()

def registrar_usuario():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    dni = input("Ingrese su DNI: ")
    correo = input("Ingrese su correo electrónico: ")
    fecha_nacimiento = input("Ingrese su fecha de nacimiento: ")
    
    while True:
        nombre_usuario = input("Ingrese un nombre de usuario (6-12 caracteres): ")
        if 6 <= len(nombre_usuario) <= 12 and nombre_usuario not in usuarios:
            break
        print("El nombre de usuario no cumple los requisitos o ya está en uso.")
    
    while True:
        clave = input("Ingrese una contraseña: ")
        if validar_clave(clave):
            break
        print("La contraseña no cumple los requisitos.")

    usuarios[nombre_usuario] = {"nombre": nombre, "apellido": apellido, "dni": dni, "correo": correo, "clave": clave}
    print("Usuario registrado con éxito.")

def validar_clave(clave):
    if (len(clave) >= 8 and 
        re.search(r"[a-z]", clave) and 
        re.search(r"[A-Z]", clave) and 
        re.search(r"\d", clave) and 
        re.search(r"\W", clave)):
        return True
    return False

bienvenida()
