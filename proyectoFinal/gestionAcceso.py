import pickle
from datetime import datetime

class Acceso:
    def __init__(self, id, fechaIngreso, usuarioLogueado):
        self.id = id
        self.fechaIngreso = fechaIngreso
        self.fechaSalida = None
        self.usuarioLogueado = usuarioLogueado

class GestionAcceso:
    def __init__(self):
        self.accesos = []
        self.cargar_accesos()

    def cargar_accesos(self):
        try:
            with open('accesos.ispc', 'rb') as f:
                self.accesos = pickle.load(f)
        except (FileNotFoundError, EOFError):
            self.accesos = []

    def guardar_accesos(self):
        with open('accesos.ispc', 'wb') as f:
            pickle.dump(self.accesos, f)

    def registrar_acceso(self, acceso):
        self.accesos.append(acceso)
        self.guardar_accesos()

    def registrar_intento_fallido(self, username, password):
        with open('logs.txt', 'a') as log:
            log.write(f"Intento fallido el {datetime.now()}. Usuario: {username}. Password: {password}\n")

    def mostrar_accesos(self):
        if not self.accesos:
            print("No hay accesos registrados.")
            return
        for acceso in self.accesos:
            print(f"ID: {acceso.id}, FechaIngreso: {acceso.fechaIngreso}, "
                  f"FechaSalida: {acceso.fechaSalida}, Usuario logueado: {acceso.usuarioLogueado}")
            