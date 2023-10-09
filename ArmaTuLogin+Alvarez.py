import time
import sys
import os
import keyboard



# Función para limpiar pantalla
def limpiar():
    if os.name=="nt": #Si fuese Windows
        os.system('cls')
    else:
        os.system('clear') #Si fuese Unix/Linux/Mac


# Función para crear usuarios.
usuarios = {}
def CrearUsuario():
    limpiar()

    while True:

        NombreUsuario = input("\nIngrese Correo electrónico - Usuario (o presionar ENTER para Salir): ")
        
        if not NombreUsuario:
            break #Acá detendrá el programa si se ha presionado Enter.
        elif NombreUsuario in usuarios:
            print(f"\n\nLa cuenta {NombreUsuario}, ya existe!\n\n")
            time.sleep(2)
            break
    
        ClaveUsuario = input("\nIngrese una Password (Clave): ")
        
        usuarios[NombreUsuario]=ClaveUsuario # Asigna la Password al usuario

        print(f"\n\n\t¡Se ha creado el usuario: {NombreUsuario}, con éxito!\n\n")
        print(usuarios)
        time.sleep(1)
        limpiar()
    

# Función para loguearse
def Login():
    limpiar()
    
    NombreUsuario = input("\nIngresa tu correo electrónico (Usuario): ")
    ClaveUsuario = input("\nIngresa tu contraseña: ") if NombreUsuario in usuarios else "Mensaje de error"
    
    if NombreUsuario in usuarios and usuarios[NombreUsuario] == ClaveUsuario:
        print(f"\n\nBienvenido {NombreUsuario} a tu sesión.")  
        time.sleep(1)
        programa()
    else:
        print("\n\nNombre de usuario o contraseña incorrectos.")
        time.sleep(1)

# Función para desplegar lista de usuarios
def ListaUsuarios():
    limpiar()
    if len(usuarios) == 0:
        print("\n\n¡No existen registros que listar!\n")
        time.sleep(2)
    else:
        for clave in usuarios:
            password = "*" * len(usuarios[clave])
            print(f"Usuario: {clave}\t Password: {password}")
        
        print("\n\nPresione 'ESC' para salir\n")
        keyboard.wait('esc')

# Función para borrar un Usuario
def BorrarUsuario():
    limpiar()
    NombreUsuario = input("\nIngrese el nombre de usuario / correo que sea borrar: ")
    if NombreUsuario in usuarios:
        del usuarios[NombreUsuario]
        print(f"\n\n\tEl usuario {NombreUsuario} ha sido eliminado.\n\n")
        time.sleep(1)
    else:
        print("\n\n\tNombre de usuario no ha sido encontratdo!!\n\n")
        time.sleep(1)

def programa():
    limpiar()
    print("\n\n\t¡Acá está corriendo 'El Programa'!\n\n") #Este es un mensaje del resultado del login
    sys.exit()


# Menu Principal

while True:
    try:
        limpiar()
        print("Opciones de Menú: \n")
        print("1. Crear usuario.")
        print("2. Ingresar al sistema.")
        print("3. Borrar usuario.")
        print("4. Ver lista de usuarios.")
        print("5. Salir.")
        opcion = input("\n\tDigite su opción (1/2/3/4/5): ")
        if opcion == "1":
            CrearUsuario()
        elif opcion == "2":
            Login()
        elif opcion == "3":
            BorrarUsuario()
        elif opcion == "4":
            ListaUsuarios()
        elif opcion == "5" or opcion == "\n":
            print("\n\nSaliendo del programa. ¡Hasta luego!")
            time.sleep(1)
            limpiar()
            break
        else:
            print("\n\nPor favor, refiérase a las opciones disponibles.")
            time.sleep(1)
            limpiar()
    except ValueError:
        print("\n\nRefiérase a las Opciones ofrecidas.")
        time.sleep(1)
        limpiar()