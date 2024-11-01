import pickle
import sys
from gestionUsuario import Usuarios
from gestionAcceso import GestionAcceso
import baseDeDatos 
import inicioSesion  
import gestionDatosPluviales
import consultas
from colorama import init, Fore, Style
import json

init(autoreset=True)

# Instancia de clases principales
ejecutar = Usuarios()
gestion_acceso = GestionAcceso()

# Funciones de carga y búsqueda de usuarios
def cargar_usuarios(filename="usuarios.ispc"):
    try:
        # Cambiar de JSON a pickle para la lectura
        with open(filename, 'rb') as file:  # Cambiar 'r' a 'rb' para lectura binaria
            usuarios = pickle.load(file)
            # Convertir el diccionario de usuarios a lista para mantener la compatibilidad
            return list(usuarios.values())
    except FileNotFoundError:
        print("El archivo no existe.")
        return []
    except Exception as e:
        print(f"Error al cargar usuarios: {e}")
        return []

def ordenar_usuarios_burbuja():
    usuarios = cargar_usuarios()
    if not usuarios:  # Verificar si hay usuarios
        print("No hay usuarios para ordenar.")
        return
        
    n = len(usuarios)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Acceder al username usando el método get_username()
            if usuarios[j].get_username() > usuarios[j + 1].get_username():
                usuarios[j], usuarios[j + 1] = usuarios[j + 1], usuarios[j]
    
    # Guardar en formato pickle
    try:
        with open("usuariosOrdenadosPorUsername.ispc", "wb") as file:  # Cambiar 'w' a 'wb'
            pickle.dump(usuarios, file)
        print("Usuarios ordenados y guardados en usuariosOrdenadosPorUsername.ispc.")
    except Exception as e:
        print(f"Error al guardar usuarios ordenados: {e}")

# También necesitamos actualizar las funciones de búsqueda
def buscar_usuario_por_dni(dni):
    usuarios = cargar_usuarios()
    return next((usuario for usuario in usuarios if str(usuario.get_dni()) == str(dni)), None)

def buscar_usuario_por_username(username):
    usuarios = cargar_usuarios()
    return next((usuario for usuario in usuarios if usuario.get_username() == username), None)

def buscar_usuario_por_email(email):
    usuarios = cargar_usuarios()
    return next((usuario for usuario in usuarios if usuario.get_email() == email), None)

# Submenús específicos
def submenu_busqueda():
    while True:
        print(Fore.CYAN + "\n--- Submenú de Búsqueda de Usuarios ---")
        print(Fore.YELLOW + "1. Buscar usuario por DNI.")
        print(Fore.YELLOW + "2. Buscar usuario por username.")
        print(Fore.YELLOW + "3. Buscar usuario por email.")
        print(Fore.YELLOW + "4. Volver al menú anterior.")

        opcion_busqueda = input(Fore.GREEN + "Ingrese su opción: ")
        if opcion_busqueda == "1":
            dni = input(Fore.GREEN + "Ingrese el DNI del usuario: ")
            usuario = buscar_usuario_por_dni(dni)
            if usuario:
                print(Fore.CYAN + 
                f"""
                Datos del usuario:
                ID: {usuario.get_id()}
                Username: {usuario.get_username()}
                DNI: {usuario.get_dni()}
                Email: {usuario.get_email()}
                """)
        elif opcion_busqueda == "2":
            username = input(Fore.GREEN + "Ingrese el username del usuario: ")
            usuario = buscar_usuario_por_username(username)
            if usuario:
                print(Fore.CYAN + 
                f"""
                    Datos del usuario:
                    ID: {usuario.get_id()}
                    Username: {usuario.get_username()}
                    DNI: {usuario.get_dni()}
                    Email: {usuario.get_email()}
                """)
            else:
                print(Fore.RED + "Usuario no encontrado.")

        elif opcion_busqueda == "3":
            email = input(Fore.GREEN + "Ingrese el email del usuario: ")
            usuario = buscar_usuario_por_email(email)
            if usuario:
                print(Fore.CYAN + 
                f"""
                Datos del usuario:
                ID: {usuario.get_id()}
                Username: {usuario.get_username()}
                DNI: {usuario.get_dni()}
                Email: {usuario.get_email()}
                """)
        elif opcion_busqueda == "4":
            break
        else:
            print(Fore.RED + "Opción incorrecta. Ingrese otra.")

def menu_ordenamiento():
    while True:
        print(Fore.CYAN + "\n--- Menú de Ordenamiento de Usuarios ---")
        print(Fore.YELLOW + "1. Ordenar los Usuarios.")
        print(Fore.YELLOW + "2. Buscar y Mostrar los Usuarios.")
        print(Fore.YELLOW + "3. Volver al menú principal.")

        opcion = input(Fore.GREEN + "Ingrese su opción: ")
        if opcion == "1":
            ordenar_usuarios_burbuja()
        elif opcion == "2":
            submenu_busqueda()
        elif opcion == "3":
            break
        else:
            print(Fore.RED + "Opción incorrecta. Ingrese otra.")

# Menús principales
def menu_principal():
    while True:
        print(Fore.CYAN + "\n--- Menú Principal ---")
        print(Fore.YELLOW + "1. Usuarios y Accesos de la Aplicación.")
        print(Fore.YELLOW + "2. Ingresar al sistema con los datos de usuario.")
        print(Fore.YELLOW + "3. Análisis de datos.")
        print(Fore.YELLOW + "4. Salir de la aplicación.")

        opcion = input(Fore.GREEN + "Ingrese su opción: ")
        if opcion == "1":
            menu_usuarios()
        elif opcion == "2":
            inicioSesion.iniciar_sesion(ejecutar, gestion_acceso)
        elif opcion == "3":
            menu_pluviales()
        elif opcion == "4":
            print(Fore.RED + "Saliendo de la aplicación...")
            sys.exit()
        else:
            print(Fore.RED + "Opción incorrecta. Ingrese otra.")

def menu_usuarios():
    while True:
        print(Fore.CYAN + "\n--- Usuarios y Accesos de la Aplicación ---")
        print(Fore.YELLOW + "1. Acceder al CRUD de los Usuarios en POO.")
        print(Fore.YELLOW + "2. Mostrar los datos de Accesos.")
        print(Fore.YELLOW + "3. Ordenamiento y Búsqueda de Usuarios.")
        print(Fore.YELLOW + "4. Volver al Menú principal.")

        opcion = input(Fore.GREEN + "Ingrese su opción: ")
        if opcion == "1":
            menu_gestion_usuarios()
        elif opcion == "2":
            menu_accesos()
        elif opcion == "3":
            menu_ordenamiento()
        elif opcion == "4":
            break
        else:
            print(Fore.RED + "Opción incorrecta. Ingrese otra.")

def menu_gestion_usuarios():
    while True:
        print(Fore.CYAN + "\n--- Menú de Gestión de Usuarios ---")
        print(Fore.YELLOW + "1. Agregar un nuevo usuario.")
        print(Fore.YELLOW + "2. Modificar un usuario.")
        print(Fore.YELLOW + "3. Eliminar un usuario.")
        print(Fore.YELLOW + "4. Volver al menú principal.")

        opcion = input(Fore.GREEN + "Ingrese su opción: ")
        if opcion == "1":
            ejecutar.agregar_usuario()
        elif opcion == "2":
            ejecutar.modificar_usuario()
        elif opcion == "3":
            ejecutar.eliminar_usuario()
        elif opcion == "4":
            break
        else:
            print(Fore.RED + "Opción incorrecta. Ingrese otra.")

def menu_accesos():
    while True:
        print(Fore.YELLOW + "1. Mostrar todos los accesos.")
        print(Fore.YELLOW + "2. Mostrar los logs de intentos fallidos.")
        print(Fore.YELLOW + "3. Salir.")
        opcion = input(Fore.GREEN + "Seleccione una opción: ")

        if opcion == '1':
            gestion_acceso.mostrar_accesos()
        elif opcion == '2':
            gestion_acceso.mostrar_intentos_fallidos()
        elif opcion == '3':
            break
        else:
            print(Fore.RED + "Opción no válida. Intentar de nuevo.")

def menu_consultas(conn):
    while True:
        print(Fore.CYAN + "\n--- Menú Base de datos: CRUD y consultas ---")
        print(Fore.YELLOW + "1. CRUD de empleados.") 
        print(Fore.YELLOW + "2. Lista completa de productos.") 
        print(Fore.YELLOW + "3. Clientes y sus direcciones.") 
        print(Fore.YELLOW + "4. Empleados activos y sus ventas.")
        print(Fore.YELLOW + "5. Resumen de ventas por área.")
        print(Fore.YELLOW + "6. Satisfacción del cliente por empleado.")
        print(Fore.YELLOW + "7. Ventas totales por empleado.") 
        print(Fore.YELLOW + "8. Productos con el stock") 
        print(Fore.YELLOW + "9. Volver.")
        
        opcion = input(Fore.GREEN + "Seleccione una opción: ")
        
        if opcion == "1":
            crud_empleados(conn)  
        elif opcion == "2":
            consultas.consulta_dos(conn)  
        elif opcion == "3":
            consultas.consulta_tres(conn)  
        elif opcion == "4":
            consultas.consulta_cuatro(conn)  
        elif opcion == "5":
            consultas.consulta_cinco(conn)  
        elif opcion == "6":
            consultas.consulta_seis(conn)  
        elif opcion == "7":
            consultas.consulta_siete(conn)  
        elif opcion == "8":
            consultas.consulta_ocho(conn) 
        elif opcion == "9":
            break
        else:
            print(Fore.RED + "Opción no válida. Intente de nuevo.")

def crud_empleados(conn):
    while True:
        print(Fore.CYAN + "\nMenú empleados:")
        print(Fore.YELLOW + "1. Agregar empleado.") 
        print(Fore.YELLOW + "2. Mostrar empleados.") 
        print(Fore.YELLOW + "3. Modificar empleado.") 
        print(Fore.YELLOW + "4. Eliminar empleado.") 
        print(Fore.YELLOW + "5. Volver al Menú Principal")
        opcion = input(Fore.GREEN + "Seleccione una opción: ")
        
        if opcion == "1":
            consultas.agregar_empleado(conn)
        elif opcion == "2":
            consultas.mostrar_empleados(conn)
        elif opcion == "3":
            consultas.modificar_empleado(conn)
        elif opcion == "4":
            consultas.eliminar_empleado(conn)
        elif opcion == "5":
            break
        else:
            print(Fore.YELLOW + "Opción no válida. Intente de nuevo.")    

def menu_pluviales():
    while True:
        print(Fore.YELLOW + "1. Cargar registros")
        print(Fore.YELLOW + "2. Salir")
        opcion = input(Fore.GREEN + "Seleccione una opción: ")

        if opcion == '1':
            gestionDatosPluviales.cargar_registros_pluviales()
        elif opcion == '2':
            break
        else:
            print(Fore.RED + "Opción no válida. Intentar de nuevo.")

# Ejecución del programa
menu_principal()
