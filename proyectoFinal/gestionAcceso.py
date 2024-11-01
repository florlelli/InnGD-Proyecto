import pickle
from datetime import datetime

class Acceso:
    def __init__(self, id, fechaIngreso, usuarioLogueado):
        self.__id = id
        self.__fechaIngreso = fechaIngreso
        self.__fechaSalida = None
        self.__usuarioLogueado = usuarioLogueado

    def get_id(self):
        return self.__id

    def get_fecha_ingreso(self):
        return self.__fechaIngreso

    def get_fecha_salida(self):
        return self.__fechaSalida

    def get_usuario_logueado(self):
        return self.__usuarioLogueado

    def set_fecha_salida(self, fechaSalida):
        self.__fechaSalida = fechaSalida

class GestionAcceso:
    def __init__(self):
        self.__accesos = []
        self.cargar_accesos()

    def cargar_accesos(self):
        try:
            with open('accesos.ispc', 'rb') as f:
                self.__accesos = pickle.load(f)
        except (FileNotFoundError, EOFError):
            self.__accesos = []

    def guardar_accesos(self):
        with open('accesos.ispc', 'wb') as f:
            pickle.dump(self.__accesos, f)

    def registrar_acceso(self, acceso):
        self.__accesos.append(acceso)
        self.guardar_accesos()

    def registrar_intento_fallido(self, username, password):
        with open('logs.txt', 'a') as log:
            log.write(f"Intento fallido el {datetime.now()}. Usuario: {username}. Password: {password}\n")

    def mostrar_accesos(self):
        if not self.__accesos:
            print("No hay accesos registrados.")
            return
        for acceso in self.__accesos:
            print(f"ID: {acceso.get_id()}, FechaIngreso: {acceso.get_fecha_ingreso()}, "
                  f"FechaSalida: {acceso.get_fecha_salida()}, Usuario logueado: {acceso.get_usuario_logueado()}")

    def get_accesos(self):
        return self.__accesos
            