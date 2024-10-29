import sys
from gestionUsuario import Usuarios
from gestionAcceso import GestionAcceso
import baseDeDatos 
import inicioSesion  
import gestionDatosPluviales
import consultas
from colorama import init, Fore, Style

init(autoreset=True)

ejecutar = Usuarios()
gestion_acceso = GestionAcceso()

def menu_principal():
    while True:
        print(Fore.CYAN + "\n--- Menú Principal ---")
        print(Fore.YELLOW + "1. Usuarios y Accesos de la Aplicación.")  
        print(Fore.YELLOW + "2. Mostrar los datos de accesos.")
        print(Fore.YELLOW + "3. Ingresar al sistema con los datos de usuario.")  
        print(Fore.YELLOW + "4. Análisis de datos.")
        print(Fore.YELLOW + "5. Salir de la palicación.")

        opcion = input(Fore.GREEN + "Ingrese su opción: ")

        if opcion == "1":
            menu_usuarios()
        elif opcion == "2":
            menu_accesos()
        elif opcion == "3":
            inicioSesion.iniciar_sesion(ejecutar, gestion_acceso)
        elif opcion == "4":
            menu_pluviales()    
        elif opcion == "5":
            print(Fore.RED + "Saliendo de la aplicación...")
            sys.exit()
        else:
            print(Fore.RED + "Opción incorrecta. Ingrese otra.")


def menu_usuarios():
    while True:
        print(Fore.CYAN + "\n--- Usuarios y Accesos de la Aplicación ---")
        print(Fore.YELLOW + "1. Acceder al CRUD de los Usuarios en POO.")  
        print(Fore.YELLOW + "2. Mostrar los datos de Accesos.")
        print(Fore.YELLOW + "3. Ordenamiento y Búsqueda de Usuarios. ")  
        print(Fore.YELLOW + "4. Volver al Menú principal. ")

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

def menu_ordenamiento():
    while True:
        print(Fore.CYAN + "\n--- Menú de Ordenamiento de Usuarios ---")
        print(Fore.YELLOW + "1. Ordenar los Usuarios. ")
        print(Fore.YELLOW + "2. Buscar y Mostrar los Usuarios.")
        print(Fore.YELLOW + "3. Volver al menú principal.")

        opcion = input(Fore.GREEN + "Ingrese su opción: ")

        if opcion == "1":
            ejecutar.ordenar_usuarios_burbuja()
        elif opcion == "2":
            print("Falta") #falta un submenu con opciones de búsqueda por dni, username o mail. 
        elif opcion == "3":
            break
        else:
            print(Fore.RED + "Opción incorrecta. Ingrese otra.") 

def menu_accesos():
      while True:
        print(Fore.YELLOW +"1. Mostrar todos los accesos. ")
        print(Fore.YELLOW +"2. Mostrar los logs de intentos fallidos. ")
        print(Fore.YELLOW +"3. Salir")
        opcion = input(Fore.GREEN + "Seleccione una opción: ")

        if opcion == '1':
            gestion_acceso.mostrar_accesos()
        elif opcion == '2':
            print("falta.") #falta mostrar los logs   
        elif opcion == '3':
            break
        else:
            print(Fore.RED + "Opción no válida. Intentar de nuevo.")  

def menu_consultas(conn):
    while True:
        print(Fore.CYAN + "\n--- Menú Base de datos: CRUD y consultas ---") 
        print(Fore.YELLOW + "1. Obtenemos todos los datos de productos.") 
        print(Fore.YELLOW + "2. Muestra los nombres de los clientes.") 
        print(Fore.YELLOW + "3. Insertar un nuevo producto.") 
        print(Fore.YELLOW + "4. Actualiza el precio de un producto.") 
        print(Fore.YELLOW + "5. Elimina una dirección.") 
        print(Fore.YELLOW + "6. Muestra los productos con sus proveedores.") 
        print(Fore.YELLOW + "7. Muestra los clientes y sus direcciones.") 
        print(Fore.YELLOW + "8. Volver.")
        
        opcion = input(Fore.GREEN + "Seleccione una opción: ")
        
        if opcion == "1":
            consultas.consulta_uno(conn)  
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
            break
        else:
            print(Fore.RED + "Opción no válida. Intente de nuevo.")

def menu_pluviales():
    while True:
        print(Fore.YELLOW +"1. Cargar registros ")
        print(Fore.YELLOW +"2. Salir")
        opcion = input(Fore.GREEN + "Seleccione una opción: ")

        if opcion == '1':
            gestionDatosPluviales.cargar_registros_pluviales()
        elif opcion == '2':
            break
        else:
            print(Fore.RED + "Opción no válida. Intentar de nuevo.")

menu_principal()