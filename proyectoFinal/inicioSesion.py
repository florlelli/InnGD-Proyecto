from datetime import datetime
from gestionAcceso import Acceso
import baseDeDatos
import mysql.connector

def iniciar_sesion(usuarios, gestion_acceso):
    username = input("Ingrese el username: ")
    password = input("Ingrese la password: ")
    if username in usuarios.usuarios:
        if usuarios.usuarios[username].get_password() == password:
            print("Ingresó correctamente.")
            fechaIngreso = datetime.now()
            acceso = Acceso(len(gestion_acceso.accesos) + 1, fechaIngreso, username)
            gestion_acceso.registrar_acceso(acceso)
            print("Llamando al menú de acceso...")  # Para depuración
            menu_acceso()  # Aquí se llama al menú de acceso
            print("Debería haber salido del menú de acceso.")  # Para depuración
        else:
            gestion_acceso.registrar_intento_fallido(username, password)
            print("Password incorrecta.")
    else:
        gestion_acceso.registrar_intento_fallido(username, password)
        print("El username no está registrado.")

def menu_acceso():
    from menu_principal import menu_consultas
    try: 
        while True:
            print("Ha ingresado al sistema.")
            print("1. Gestionar la base de datos.")
            print("2. Volver al menú principal.")
            print("3. Salir de la aplicación.")
            opcion = input("Ingrese su opción: ")
            if opcion == "1":
                user_base = input("Ingrese su usuario de MySQL Workbench: ")
                pass_base = input("Ingrese su contraseña de MySQL Workbench: ")
                
                # Intentar conectar a la base de datos
                try:
                    conn = baseDeDatos.obtener_conexion(user_base, pass_base)
                    print("Conexión a la base de datos exitosa.")
                    # Aquí puedes llamar a menu_consultas o cualquier otra función para gestionar la base de datos
                    menu_consultas(conn)  # Asumiendo que se pasa la conexión a este menú
                except mysql.connector.Error as err:
                    print(f"Error: {err}")
            
            elif opcion == "2":
                return
            elif opcion == "3":
                print("Salió del sistema.")
                exit()  # Cambié sys.exit() por exit() para simplificar
            else:
                print("Opción incorrecta. Ingrese otra.")
    except Exception as e:
        print(f"Ocurrió un error en menu_acceso: {e}")