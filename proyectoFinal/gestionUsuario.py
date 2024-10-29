from gestionAcceso import Acceso
import pickle
from datetime import datetime
import sys #para salir del sistema

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

class Usuarios:  #para crud de los usuarios
    def __init__(self):      
        self.usuarios = {} 
        self.accesos = [] 
        self.usuarios_ordenados = False  # Nuevo atributo para rastrear si los usuarios están ordenados
        self.cargar_usuarios() 
        self.cargar_accesos()
        
    def cargar_usuarios(self):
        try:
            with open('usuarios.ispc', 'rb') as f: 
                self.usuarios = pickle.load(f) 
        except (FileNotFoundError, EOFError): 
            self.usuarios = {} 

    def guardar_usuarios(self):
        with open('usuarios.ispc', 'wb') as f: 
            pickle.dump(self.usuarios, f) 

    def cargar_accesos(self):
        try:
            with open('accesos.ispc', 'rb') as f:
                self.accesos = pickle.load(f)
        except (FileNotFoundError, EOFError):
            self.accesos = []

    def guardar_accesos(self):
        with open('accesos.ispc', 'wb') as f:
            pickle.dump(self.accesos, f)

#--------------------------------------- ORDENAMIENTO ----------------------------------------------------------------------
    def ordenar_usuarios_burbuja(self):
        usuarios_list = list(self.usuarios.values())
        n = len(usuarios_list)
        for i in range(n):
            for j in range(0, n - i - 1):
                if usuarios_list[j].get_username() > usuarios_list[j + 1].get_username():
                    usuarios_list[j], usuarios_list[j + 1] = usuarios_list[j + 1], usuarios_list[j]
        
        self.usuarios = {user.get_username(): user for user in usuarios_list}
        self.guardar_usuarios()  
        self.usuarios_ordenados = True  
        print("Usuarios ordenados por burbuja y guardados en usuarios.ispc.")

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
        self.usuarios_ordenados = False
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
        username = input("Ingrese el username del usuario a eliminar: ")
        if username in self.usuarios:
            del self.usuarios[username]  
            self.guardar_usuarios()  
            self.usuarios_ordenados = False
            print(f"Usuario {username} eliminado correctamente.")
        else:
            print(f"No existe el usuario con username {username}.")

# -------------------------------- BÚSQUEDAS ----------------------------------------------------------
    def buscar_usuario(self):
        username = input("Ingrese el username del usuario a buscar: ")
        if self.usuarios_ordenados:
            print("Búsqueda realizada por técnica de búsqueda binaria.")
            resultado = self.busqueda_binaria(username)
        else:
            print("Búsqueda realizada por técnica de búsqueda secuencial.")
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

    def busqueda_binaria(self, username):
        usuarios_list = sorted(self.usuarios.values(), key=lambda user: user.get_username())
        low, high = 0, len(usuarios_list) - 1

        while low <= high:
            mid = (low + high) // 2
            if usuarios_list[mid].get_username() == username:
                return usuarios_list[mid]
            elif usuarios_list[mid].get_username() < username:
                low = mid + 1
            else:
                high = mid - 1
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