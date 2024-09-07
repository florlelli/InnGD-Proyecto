import re #importamos el módulo re ya que vamos a usar expresiones regulares. 
from captchas import Captcha

class Usuarios:  
    def __init__(self):      
        self.usuarios = {}
        self.captcha = Captcha()

    def validar_contraseña(self, contraseña):  
        una_minuscula = re.compile(r'[a-z]') #este patrón va a buscar cualquier letra minúscula (especificadas en los corchetes) 
        una_mayuscula = re.compile(r'[A-Z]') #va a buscar cualquier letra mayúscula
        un_num = re.compile(r'[0-9]') #va a buscar cualquier número del 0 al 9
        un_especial = re.compile(r'[^a-zA-Z0-9_]') #se usa para buscar caracteres especiales
        #un if para que si cada una de esas busquedas nos devuelve algo, nos de un True.
        if una_minuscula.search(contraseña) and una_mayuscula.search(contraseña) and un_num.search(contraseña) and un_especial.search(contraseña) and len(contraseña) >= 8:
            return True 
        return False
        #La función search en re encuentra la primera coincidencia, que asegura que al menos uno de cada tipo de carácter esté presente.

    def validar_usuario(self, usuario):
        if len(usuario) < 6 or len(usuario) > 12:
            print("El nombre de usuario debe tener entre 6 y 12 caracteres.")
            return False #si el usuario es menor a 5 o mayor a 12 va a dar falso.
        if usuario in self.usuarios:
            print("Ya hay un usuario registrado con ese nombre de usuario.")
            return False
        return True #si los ifs no se cumplen (o sea las validaciones dan bien), va a dar verdadero. 

    def captcha_validado(self):
        while True: #un ciclo para que se repita hasta que sea correcto.
            resultado = self.captcha.generar_captcha() #llamamos la función generar captcha y guardamos el resultado de la operación en la variable resultado
            try:
                respuesta = float(input("Ingrese el resultado: "))
                if round(respuesta, 2) == resultado: #si lo que ingresó el usario es igual al resultado de la función del captcha, devuleve un true.
                    return True #termina el ciclo.
                else: #si no es igual, imprime el mensaje y el ciclo se repite. 
                    print("Respuesta incorrecta. Intente de nuevo.")
            except ValueError: #si el usuario ingresa un valor que no sea un número float abre la excepción.
                print("Error valor inválido.")

    def ingresar_usuario(self):
        usuario = input("Ingrese el usuario: ")
        contraseña = input("Ingrese la contraseña: ")
        if usuario in self.usuarios: #verifica que el suario esté en el diccionario de usuarios. 
          if self.usuarios[usuario]['contraseña'] == contraseña: #verifica que la contraseña de ese usuario exista y esté asociada al usuario.
               print("Ingresó correctamente.")
          else:
            print("Contraseña incorrecta.")
        else:
         print("El usuario no está registrado.")


    def registrar_usuario(self): 
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        while True: #ciclo para que siga pidiendo el usuario hasta que las validaciones estén correctas. 
            usuario = input("Ingrese su nombre de usuario: ")
            if self.validar_usuario(usuario): #si la función devuelve un true, tiene el breack. Sino, se repite el ciclo. 
                break              
        dni = input("Ingrese su dni: ")
        while any(user['dni'] == dni for user in self.usuarios.values()): #any() devuelve true si al menos uno de los elementos del dic es true, o sea si está ahí.
        #Para cada valor, verifica si el valor asociado a la clave dni es igual al ingresado. values() devuelve una vista de todos los valores en el diccionario   
            dni = input("Ya hay un usuario registado con ese DNI. Ingrese otro: ")
        correo = input("Ingrese su correo: ")
        fecha_nacimiento = input("Ingrese su fecha de nacimiento: ")
        contraseña = input("La contraseña debe tener un mínimo de 8 caracteres y contener al menos dos de las siguientes condiciones: \ni. Al menos 1 minúscula.\nii. Al menos 1 mayúscula. \niii. Al menos 1 número. \niv. Al menos un caracter especial (caracter que no es letra ni número).\n\nIngrese la contraseña: ")
        
        while not self.validar_contraseña(contraseña): #usamos la función de validación. Se ejecuta hasta que el false se haga true. 
            print("La contraseña no cumple con los requisitos.\nLa contraseña debe tener un mínimo de 8 caracteres y contener al menos dos de las siguientes condiciones: \ni. Al menos 1 minúscula.\nii. Al menos 1 mayúscula. \niii. Al menos 1 número. \niv. Al menos un caracter especial (caracter que no es letra ni número).\n")
            contraseña = input("Ingrese la contraseña: ")
        

        if not self.captcha_validado():
            print("Captcha inválido.")
            return

        self.usuarios[usuario] = {"nombre": nombre, #guardamos todos los datos en el diccionario, tomando el usuario como clave. 
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
