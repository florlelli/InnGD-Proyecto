from datetime import datetime
from gestionAcceso import Acceso
import baseDeDatos
import mysql.connector
from colorama import init, Fore, Style

def iniciar_sesion(usuarios, gestion_acceso):
    username = input("Ingrese el username: ")
    password = input("Ingrese la password: ")
    if username in usuarios.usuarios:
        if usuarios.usuarios[username].get_password() == password:
            print("Ingresó correctamente.")
            fechaIngreso = datetime.now()
            acceso = Acceso(len(gestion_acceso.get_accesos()) + 1, fechaIngreso, username)
            gestion_acceso.registrar_acceso(acceso)
            print("Llamando al menú de acceso...")
            menu_acceso(gestion_acceso, acceso)  
        else:
            gestion_acceso.registrar_intento_fallido(username, password)
            print("Password incorrecta.")
    else:
        gestion_acceso.registrar_intento_fallido(username, password)
        print("El username no está registrado.")

def menu_acceso(gestion_acceso, acceso_actual):
    from main import menu_consultas  
    try: 
        while True:
            print(Fore.CYAN + "Ha ingresado al sistema.")
            print(Fore.YELLOW + "1. Gestionar la base de datos.")
            print(Fore.YELLOW + "2. Volver al menú principal.")
            print(Fore.YELLOW + "3. Salir de la aplicación.")
            opcion = input(Fore.GREEN + "Ingrese su opción: ")

            if opcion == "1":
                user_base = input("Ingrese su usuario de MySQL Workbench: ")
                pass_base = input("Ingrese su contraseña de MySQL Workbench: ")
                
                try:
                    conn = baseDeDatos.obtener_conexion(user_base, pass_base)
                    print(Fore.BLUE + "Conexión a la base de datos exitosa.")
                    menu_consultas(conn)
                except mysql.connector.Error as err:
                    print(f"Error: {err}")
            
            elif opcion == "2":
                return
            elif opcion == "3":
                acceso_actual.set_fecha_salida(datetime.now()) 
                gestion_acceso.guardar_accesos()  
                print(Fore.RED + "Salió del sistema.")
                exit()  
            else:
                print("Opción incorrecta. Ingrese otra.")
    except Exception as e:
        print(f"Ocurrió un error en menu_acceso: {e}")