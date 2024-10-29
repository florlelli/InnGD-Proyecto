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
        print(Fore.YELLOW + "1. Gestión de usuarios.")  
        print(Fore.YELLOW + "2. Mostrar los datos de accesos.")
        print(Fore.YELLOW + "3. Ingresar al sistema e ir a la base de datos.")  
        print(Fore.YELLOW + "4. Datos pluviales.")
        print(Fore.YELLOW + "5. Salir.")

        opcion = input(Fore.GREEN + "Ingrese su opción: ")

        if opcion == "1":
            menu_gestion_usuarios()
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

def menu_gestion_usuarios():
    while True:
        print(Fore.CYAN + "\n--- Menú de Gestión de Usuarios ---")
        print(Fore.YELLOW + "1. Agregar un nuevo usuario.")
        print(Fore.YELLOW + "2. Modificar un usuario.")
        print(Fore.YELLOW + "3. Eliminar un usuario.")
        print(Fore.YELLOW + "4. Buscar un usuario.")
        print(Fore.YELLOW + "5. Mostrar todos los usuarios.")
        print(Fore.YELLOW + "6. Ordenar usuarios por burbuja y guardar.")
        print(Fore.YELLOW + "7. Volver al menú principal.")

        opcion = input(Fore.GREEN + "Ingrese su opción: ")

        if opcion == "1":
            ejecutar.agregar_usuario()
        elif opcion == "2":
            ejecutar.modificar_usuario()
        elif opcion == "3":
            ejecutar.eliminar_usuario()
        elif opcion == "4":
            ejecutar.buscar_usuario()
        elif opcion == "5":
            ejecutar.mostrar_usuarios()
        elif opcion == "6":
            ejecutar.ordenar_usuarios_burbuja() 
        elif opcion == "7":
            break
        else:
            print(Fore.RED + "Opción incorrecta. Ingrese otra.")

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
        
        opcion = input("Seleccione una opción: ")
        
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
            print("Opción no válida. Intente de nuevo.")

def menu_pluviales():
    while True:
        print("1. Cargar registros ")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            gestionDatosPluviales.cargar_registros_pluviales()
        elif opcion == '2':
            print("Salir del programa.")
            break
        else:
            print("Opción no válida. Intentar de nuevo.")

def menu_accesos():
      while True:
        print("1. Mostrar todos los accesos. ")
        print("2. Mostrar los logs de intentos fallidos. ")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            gestion_acceso.mostrar_accesos()
        elif opcion == '2':
            print("falta.")    
        elif opcion == '3':
            print("Salir del programa.")
            break
        else:
            print("Opción no válida. Intentar de nuevo.")  


menu_principal()
