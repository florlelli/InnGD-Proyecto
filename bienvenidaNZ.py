import re

# Diccionario para almacenar los usuarios
usuarios = {}

def mostrar_bienvenida():
    print("------------------------------------------")
    print("¡Bienvenido a la aplicación de gestión de usuarios!")
    print("------------------------------------------")

def validar_clave(clave):
    if len(clave) < 8:
        return False
    condiciones = [r'[a-z]', r'[A-Z]', r'\d', r'\W']
    return sum(bool(re.search(cond, clave)) for cond in condiciones) >= 2

def validar_usuario(nombre_usuario):
    return 6 <= len(nombre_usuario) <= 12

def registrar_usuario():
    print("\nRegistro de nuevo usuario:")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("DNI: ")
    correo = input("Correo electrónico: ")
    fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
    nombre_usuario = input("Nombre de usuario: ")

    # Validar que el DNI y el nombre de usuario sean únicos
    if dni in [usuario['dni'] for usuario in usuarios.values()]:
        print("Error: El DNI ya está registrado.")
        return
    
    if nombre_usuario in usuarios:
        print("Error: El nombre de usuario ya está registrado.")
        return
    
    if not validar_usuario(nombre_usuario):
        print("Error: El nombre de usuario debe tener entre 6 y 12 caracteres.")
        return
    
    clave = input("Clave: ")
    
    if not validar_clave(clave):
        print("Error: La clave debe tener al menos 8 caracteres y contener al menos dos de los siguientes: minúsculas, mayúsculas, números o caracteres especiales.")
        return

    # Registrar usuario
    usuarios[nombre_usuario] = {
        'nombre': nombre,
        'apellido': apellido,
        'dni': dni,
        'correo': correo,
        'fecha_nacimiento': fecha_nacimiento,
        'nombre_usuario': nombre_usuario,
        'clave': clave
    }
    print("Usuario registrado exitosamente.")

def inicio_sesion():
    print("\nInicio de sesión:")
    nombre_usuario = input("Nombre de usuario: ")
    clave = input("Clave: ")
    
    usuario = usuarios.get(nombre_usuario)
    
    if usuario and usuario['clave'] == clave:
        print(f"¡Hola {usuario['nombre']} {usuario['apellido']}!")
    else:
        print("Error: Usuario o clave incorrectos.")

def main():
    mostrar_bienvenida()
    
    while True:
        print("\nOpciones:")
        print("1. Iniciar sesión")
        print("2. Registrar nuevo usuario")
        print("3. Salir")
        opcion = input("Seleccione una opción (1/2/3): ")
        
        if opcion == '1':
            inicio_sesion()
        elif opcion == '2':
            registrar_usuario()
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
