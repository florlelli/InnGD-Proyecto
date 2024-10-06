from clases import Usuarios

usuarios = Usuarios() #instanciamos la clase

def menu_usuarios():
        while True:
            print("1. Agregar un nuevo usuario. ")
            print("2. Modificar un usuario. ")
            print("3. Eliminar un usuario. ")
            print("4. Buscar un usuario. ")
            print("5. Mostrar todos los usuarios. ")
            print("6. Mostrar accesos. ")
            print("7. Volver. ")
            opcion = int(input("Ingrese su opción: "))  
            if opcion == 1:
                usuarios.agregar_usuario()
            elif opcion == 2:
                usuarios.modificar_usuario()
            elif opcion == 3:
                usuarios.eliminar_usuario()
            elif opcion == 4:
                usuarios.buscar_usuario()
            elif opcion == 5:
                usuarios.mostrar_usuarios()
            elif opcion == 6:
                usuarios.mostrar_accesos()
            elif opcion == 7:
                return
            else:
                print("Opción incorrecta. Ingrese otra. ")

while True: 
    print("----- BIENVENIDA -----")
    print("1. Gestión de usuarios. ")
    print("2. Ingresar al sistema. ")
    print("3. Salir. ")
    opcion = int(input("Ingrese su opción: "))  
    if opcion == 1:
        menu_usuarios()
    elif opcion == 2:
        usuarios.ingresar_usuario()
    elif opcion == 3:
        break
    else:
            print("Opción incorrecta. Ingrese otra. ")




