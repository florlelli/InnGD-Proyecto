import re #importamos el módulo re ya que vamos a usar expresiones regulares. 
from captchas import Captcha

class Usuarios:  
    def __init__(self):      
        self.usuarios = {}
        self.captcha = Captcha()

    def validar_contraseña(self, contraseña):
     if (len(contraseña) >= 8 and 
        re.search(r"[a-z]", contraseña) and 
        re.search(r"[A-Z]", contraseña) and 
        re.search(r"\d", contraseña) and 
        re.search(r"\W", contraseña)):
        return True
     return False

    def validar_usuario(self, usuario):
        if len(usuario) < 6 or len(usuario) > 12:
            print("El nombre de usuario debe tener entre 6 y 12 caracteres.")
            return False 
        if usuario in self.usuarios:
            print("Ya hay un usuario registrado con ese nombre de usuario.")
            return False
        return True 

    def captcha_validado(self):
        while True: 
            resultado = self.captcha.generar_captcha() 
            try:
                respuesta = float(input("Ingrese el resultado: "))
                if round(respuesta, 2) == resultado: 
                    return True 
                else: 
                    print("Respuesta incorrecta. Intente de nuevo.")
            except ValueError: 
                print("Error valor inválido.")

    def ingresar_usuario(self):
        usuario = input("Ingrese el usuario: ")
        contraseña = input("Ingrese la contraseña: ")
        if usuario in self.usuarios: 
          if self.usuarios[usuario]['contraseña'] == contraseña: 
               print("Ingresó correctamente.")
          else:
            print("Contraseña incorrecta.")
        else:
         print("El usuario no está registrado.")


    def registrar_usuario(self): 
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        while True: 
            usuario = input("Ingrese su nombre de usuario: ")
            if self.validar_usuario(usuario): 
                break              
        dni = input("Ingrese su dni: ")
        while any(user['dni'] == dni for user in self.usuarios.values()):    
            dni = input("Ya hay un usuario registado con ese DNI. Ingrese otro: ")
        correo = input("Ingrese su correo: ")
        fecha_nacimiento = input("Ingrese su fecha de nacimiento: ")
        
        print("La contraseña debe tener un mínimo de 8 caracteres y contener al menos dos de las siguientes condiciones: \ni. Al menos 1 minúscula.\nii. Al menos 1 mayúscula. \niii. Al menos 1 número. \niv. Al menos un caracter especial (caracter que no es letra ni número).\n")
        while True:
            contraseña = input("Ingrese una contraseña: ")
            if self.validar_contraseña(contraseña):
                break
            print("La contraseña no cumple los requisitos.")
        
        if not self.captcha_validado():
            print("Captcha inválido.")
            return

        self.usuarios[usuario] = {"nombre": nombre, 
                              "apellido": apellido, 
                              "dni" : dni,
                              "correo": correo, 
                              "fecha de nacimiento": fecha_nacimiento,
                              "usuario": usuario,
                              "contraseña" : contraseña }

        print(f"\nSe registró el usuario {usuario}.")

    def mostrar_usuarios(self):
        buscar = input("Ingrese el nombre del usuario que desea buscar: ")
        print(self.usuarios[buscar])

    def bienvenida(self):
        while True: 
            print("----- BIENVENIDA -----")
            print("1. Ingresar con un usuario. ")
            print("2. Registrar un nuevo usuario. ")
            print("3. Mostrar usuarios. ")
            print("4. Salir. ")
            opcion = int(input("Ingrese su opción: "))  
            if opcion == 1:
                self.ingresar_usuario()
            elif opcion == 2:
                self.registrar_usuario()
            elif opcion == 3:
                self.mostrar_usuarios()
            elif opcion == 4:
                break
            else:
                print("Opción incorrecta. Ingrese otra. ")

ejecutar = Usuarios() #instanciamos la clase usuarios

ejecutar.bienvenida() #llamamos la función bienvenida
