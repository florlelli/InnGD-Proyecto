from gestionAcceso import Acceso
import pickle
from datetime import datetime
import sys  # Para salir del sistema

class Usuario:
    def __init__(self, id, username, dni, password, email):
        self.__id = id
        self.__username = username
        self.__dni = dni
        self.__password = password
        self.__email = email

    def get_id(self):
        return self.__id

    def get_username(self):
        return self.__username

    def get_dni(self):
        return self.__dni

    def get_password(self):
        return self.__password

    def get_email(self):
        return self.__email

    def set_username(self, username):
        self.__username = username

    def set_dni(self, dni):
        self.__dni = dni

    def set_password(self, password):
        self.__password = password

    def set_email(self, email):
        self.__email = email

class Usuarios:  # Para CRUD de los usuarios
    def __init__(self):      
        self.usuarios = {} 
        self.cargar_usuarios() 
        
    def cargar_usuarios(self):
        try:
            with open('usuarios.ispc', 'rb') as f: 
                self.usuarios = pickle.load(f) 
        except (FileNotFoundError, EOFError): 
            self.usuarios = {} 

    def guardar_usuarios(self):
        with open('usuarios.ispc', 'wb') as f: 
            pickle.dump(self.usuarios, f) 

# --------------------------------------- CRUDS ----------------------------------------------------------------------
    def agregar_usuario(self): 
        id = len(self.usuarios) + 1 
        username = input("Ingrese su username: ")
        while username in self.usuarios:
            print("Ya hay un usuario registrado con ese username.")
            username = input("Ingrese su username: ")
        while True:
            try:
                dni = int(input("Ingrese su dni: "))
                if dni in [user.get_dni() for user in self.usuarios.values()]:
                    print("Ya hay un usuario registrado con ese dni.")
                else:
                    break 
            except ValueError:
                print("No ingresó un número. Intente otra vez.")
        email = input("Ingrese su email: ")  
        password = input("Ingrese una password: ")
        self.usuarios[username] = Usuario(id, username, dni, password, email)  
        self.guardar_usuarios() 
        print(f"\nSe registró el usuario {username}.")

    def modificar_usuario(self):
        username = input("Ingrese el username del usuario a modificar: ")
        if username in self.usuarios:
            email = input(f"Nuevo email para {username}: ")
            password = input(f"Nueva password para {username}: ")
            self.usuarios[username].set_email(email)
            self.usuarios[username].set_password(password)
            self.guardar_usuarios()  
            print(f"Usuario {username} modificado exitosamente.")
        else:
            print(f"No existe el usuario con username {username}.")

    def eliminar_usuario(self):
        opcion = input("Eliminar usuario por: \n1. Username \n2. Email \nIngrese 1 o 2: ")
        if opcion == '1':
            username = input("Ingrese el username del usuario a eliminar: ")
            if username in self.usuarios:
                del self.usuarios[username]  
                self.guardar_usuarios()  
                print(f"Usuario {username} eliminado correctamente.")
            else:
                print(f"No existe el usuario con username {username}.")
        elif opcion == '2':
            email = input("Ingrese el email del usuario a eliminar: ")
            usuario_encontrado = None
            for usuario in self.usuarios.values():
                if usuario.get_email() == email:
                    usuario_encontrado = usuario
                    break
            if usuario_encontrado:
                username = usuario_encontrado.get_username()
                del self.usuarios[username]  
                self.guardar_usuarios()  
                print(f"Usuario con email {email} eliminado correctamente.")
            else:
                print(f"No existe un usuario con el email {email}.")
        else:
            print("Opción no válida. Intente de nuevo.")

# -------------------------------- BÚSQUEDAS ----------------------------------------------------------
    def buscar_usuario(self):
        username = input("Ingrese el username del usuario a buscar: ")
        resultado = self.busqueda_secuencial(username)

        if resultado:
            print(f"ID: {resultado.get_id()}, Username: {resultado.get_username()}, Email: {resultado.get_email()}")
        else:
            print("Usuario no encontrado.")

    def busqueda_secuencial(self, username):
        for user in self.usuarios.values():
            if user.get_username() == username:
                return user
        return None

    def mostrar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados.")
            return
        for usuario in self.usuarios.values(): 
            print(f"ID: {usuario.get_id()}, Usuario: {usuario.get_username()}, Email: {usuario.get_email()}")

# ----------------------------- INGRESO AL SISTEMA ----------------------------------------------------------
    def ingresar_usuario(self, gestion_acceso):
        from inicioSesion import iniciar_sesion
        iniciar_sesion(self, gestion_acceso)

ejecutar = Usuarios()