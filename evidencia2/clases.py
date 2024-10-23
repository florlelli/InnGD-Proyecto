import pickle
from datetime import datetime
import sys #para salir del sistema

class Usuario:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

class Acceso:
    def __init__(self, id, fechaIngreso, usuarioLogueado):
        self.id = id
        self.fechaIngreso = fechaIngreso
        self.fechaSalida = None 
        self.usuarioLogueado = usuarioLogueado

class Usuarios:  #para crud de los usuarios
    def __init__(self):      
        self.usuarios = {} 
        self.accesos = [] 
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

    def ordenar_usuarios_burbuja(self):
        usuarios_list = list(self.usuarios.values())  # Convertimos el diccionario de usuarios a una lista de objetos Usuario
        n = len(usuarios_list)
        for i in range(n):
            for j in range(0, n - i - 1):
                # Comparamos los usernames de los usuarios para ordenarlos
                if usuarios_list[j].username > usuarios_list[j + 1].username:
                    usuarios_list[j], usuarios_list[j + 1] = usuarios_list[j + 1], usuarios_list[j]
        
        # Volver a convertir la lista ordenada en un diccionario
        self.usuarios = {user.username: user for user in usuarios_list}
        self.guardar_usuarios()  # Guardar los usuarios ordenados en el archivo binario
        print("Usuarios ordenados por burbuja y guardados en usuarios.ispc.")
        
#CRUDS----------------------------------------------------------------------------------------------------------------
    def agregar_usuario(self): 
        id = len(self.usuarios) + 1 
        username = input("Ingrese su username: ")
        while username in self.usuarios:
            print("Ya hay un usuario registrado con ese username.")
            username = input("Ingrese su username: ")
        email = input("Ingrese su email: ")  
        password = input("Ingrese una password: ")
        self.usuarios[username] = Usuario(id, username, password, email)  
        self.guardar_usuarios() 
        print(f"\nSe registró el usuario {username}.")

    def modificar_usuario(self):
        username = input("Ingrese el username del usuario a modificar: ")
        if username in self.usuarios:
            email = input(f"Nuevo email para {username}: ")
            password = input(f"Nueva password para {username}: ")
            self.usuarios[username].email = email
            self.usuarios[username].password = password
            self.guardar_usuarios()  
            print(f"Usuario {username} modificado exitosamente.")
        else:
            print(f"No existe el usuario con username {username}.")

    def eliminar_usuario(self):
        username = input("Ingrese el username del usuario a eliminar: ")
        if username in self.usuarios:
            del self.usuarios[username]  
            self.guardar_usuarios()  
            print(f"Usuario {username} eliminado correctamente.")
        else:
            print(f"No existe el usuario con username {username}.")

    def buscar_usuario(self):
        username = input("Ingrese el username o email del usuario a buscar: ")
        for user in self.usuarios.values():
            if user.username == username or user.email == username:
                print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")
            return
        print("Usuario no encontrado.")

    def mostrar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados.")
            return
        for usuario in self.usuarios.values(): 
            print(f"ID: {usuario.id}, Usuario: {usuario.username}, Email: {usuario.email}")

    def ingresar_usuario(self):
        username = input("Ingrese el username: ")
        password = input("Ingrese la password: ")
        if username in self.usuarios: 
            if self.usuarios[username].password == password: 
                print("Ingresó correctamente.")
                fechaIngreso = datetime.now() 
                acceso = Acceso(len(self.accesos) + 1, fechaIngreso, username) 
                self.accesos.append(acceso) 
                self.guardar_accesos() 
                self.menu_acceso()  
            else:
                self.intento_fallido(username, password)
                print("Password incorrecta.")
        else:
            self.intento_fallido(username, password) 
            print("El username no está registrado.")

    def intento_fallido(self, username, password):
        with open('logs.txt', 'a') as log: 
            log.write(f"Intento fallido el {datetime.now()}. Usuario: {username}. Password: {password}\n") 

    def menu_acceso(self):
        while True:
            print("Ha ingresado al sistema.")
            print("1. Volver al menú principal. ")
            print("2. Salir del sistema.")
            opcion = input("Ingrese su opción: ")
            if opcion == "1":
                return
            elif opcion == "2":
                if self.accesos:
                    self.accesos[-1].fechaSalida = datetime.now() 
                    self.guardar_accesos() 
                    print("Salió del sistema.")
                    sys.exit()
            else:
                print("Opción incorrecta. Ingrese otra.")

    def mostrar_accesos(self):
        for acceso in self.accesos: 
            print(f"ID: {acceso.id}, FechaIngreso: {acceso.fechaIngreso}, FechaSalida: {acceso.fechaSalida}, Usuario logueado: {acceso.usuarioLogueado}")


ejecutar = Usuarios() 


