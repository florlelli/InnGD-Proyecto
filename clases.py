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
        self.usuarios = {} #crea un dic para los usuarios
        self.accesos = [] #crea una lista para los accesos
        self.cargar_usuarios() #va a intentar cargar los datos ya existentes en los archivos
        self.cargar_accesos()
        
    def cargar_usuarios(self):
        try:
            with open('usuarios.ispc', 'rb') as f: #abre el archivo como lectura en binario
                self.usuarios = pickle.load(f) #en el archvio abierto deserealiza los datos 
        except (FileNotFoundError, EOFError): #si el archivo no existe o está vacio
            self.usuarios = {} #empieza con un dic vacío. 

    def guardar_usuarios(self):
        with open('usuarios.ispc', 'wb') as f: #abre el archivo como escritura en binario
            pickle.dump(self.usuarios, f) #serealiza los datos

    def cargar_accesos(self):
        try:
            with open('accesos.ispc', 'rb') as f:
                self.accesos = pickle.load(f)
        except (FileNotFoundError, EOFError):
            self.accesos = []

    def guardar_accesos(self):
        with open('accesos.ispc', 'wb') as f:
            pickle.dump(self.accesos, f)

#CRUDS----------------------------------------------------------------------------------------------------------------
    def agregar_usuario(self): 
        id = len(self.usuarios) + 1 #hacemos el id único y autoincremental usando la longitud del diccionario
        username = input("Ingrese su username: ")
        while username in self.usuarios:
            print("Ya hay un usuario registrado con ese username.")
            username = input("Ingrese su username: ")
        email = input("Ingrese su email: ")  
        password = input("Ingrese una password: ")
        self.usuarios[username] = Usuario(id, username, password, email) #creamos una instancia para la clase Usuario guardando los datos ingresados en un dic usando como clave el username. 
        self.guardar_usuarios() #lo guarda en el archivo
        print(f"\nSe registró el usuario {username}.")

    def modificar_usuario(self):
        pass

    def eliminar_usuario(self):
        pass

    def buscar_usuario(self):
        pass

    def mostrar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados.")
            return
        for usuario in self.usuarios.values(): #va mostrando cada uno de los usuaraios en ese formato sin la pass
            print(f"ID: {usuario.id}, Usuario: {usuario.username}, Email: {usuario.email}")

    def ingresar_usuario(self):
        username = input("Ingrese el username: ")
        password = input("Ingrese la password: ")
        if username in self.usuarios: #si el usuario está en el dic usuarios
            if self.usuarios[username].password == password: #y si la password escrita es igual a la password de ese user
                print("Ingresó correctamente.")
                fechaIngreso = datetime.now() #captura la fecha de ahora en la variable fechaIngreso
                acceso = Acceso(len(self.accesos) + 1, fechaIngreso, username) #crea un objeto de acceso con:
                #id que es la longitud la lista + 1, la fecha y el username. 
                self.accesos.append(acceso) #agrega el objeto en la lista
                self.guardar_accesos() #la guarda
                self.menu_acceso()  #llama al menu de acceso
            else:
                self.intento_fallido(username, password) #llamamos la función de intento fallido cuando la pass está mal
                print("Password incorrecta.")
        else:
            self.intento_fallido(username, password) #lo mismo cuando el user está mal
            print("El username no está registrado.")

    def intento_fallido(self, username, password):
        with open('logs.txt', 'a') as log: #añade el archivo logs.txt para escritura si no existe, y si existe escribe al final
            log.write(f"Intento fallido el {datetime.now()}. Usuario: {username}. Password: {password}\n") #escribe.

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
                    self.accesos[-1].fechaSalida = datetime.now()  #actualiza la fecha de salida. El [-1] nos da el último acceso registrado, o sea el que está ahora logueado.
                    self.guardar_accesos()  #lo guarda
                    print("Salió del sistema.")
                    sys.exit()
            else:
                print("Opción incorrecta. Ingrese otra.")

    def mostrar_accesos(self):
        for acceso in self.accesos: 
            print(f"ID: {acceso.id}, FechaIngreso: {acceso.fechaIngreso}, FechaSalida: {acceso.fechaSalida}, Usuario logueado: {acceso.usuarioLogueado}")


ejecutar = Usuarios() #instanciamos la clase usuarios


