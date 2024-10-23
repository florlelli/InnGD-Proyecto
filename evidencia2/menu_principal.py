import sys
from clases import Usuarios
from colorama import init, Fore, Style


init(autoreset=True)

ejecutar = Usuarios()

def menu_principal():
    while True:
        print(Fore.CYAN + "\n--- Menú Principal ---")
        print(Fore.YELLOW + "1. Gestión de usuarios.")
        print(Fore.YELLOW + "2. Ingresar al sistema.")
        print(Fore.YELLOW + "3. Mostrar accesos.")
        print(Fore.YELLOW + "4. Salir.")

        opcion = input(Fore.GREEN + "Ingrese su opción: ")

        if opcion == "1":
            menu_gestion_usuarios()
        elif opcion == "2":
            ejecutar.ingresar_usuario()
        elif opcion == "3":
            ejecutar.mostrar_accesos()
        elif opcion == "4":
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


menu_principal()
