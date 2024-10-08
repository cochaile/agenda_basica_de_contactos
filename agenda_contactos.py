### VIDEO DESDE 6.27 hs

import email


def mostrar_menu():
    print("\nAgenda de contactos:")
    print("1. Agreagr nuevo contacto")
    print("2. Eliminar contacto existente")
    print("3. Buscar contacto")
    print("4. Lista de contactos")
    print("5. Salir del programa")
    print("\n")

def agregar_contacto(agenda):
    nombre = input("Por favor introduzca el nombre completo (Apellido y Nombre) del contacto: ")
    telefono = input("Por favor introduzca el teléfono del contacto: ")
    email = input("Por favor introduzca el email del contacto: ")
    agenda[nombre] = {"telefono":telefono,"email":email}
    print(f"¡Se ha agregado el contacto {nombre} exitosamente!")

def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"El contacto {nombre} ha sido eliminado correctamente")
    else:
        print(f"No se ha encontrado un contacto con el nombre {nombre}")

def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    if nombre in agenda:
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {agenda[nombre]["telefono"]}") # Para acceder a la clave telefono primero hay que acceder a la key nombre
        print(f"E-mail: {agenda[nombre]["email"]}") # Para acceder a la clave email primero hay que acceder a la key nombre
    else:
        print(f"El contacto {nombre} no ha sido encontrado")

def listar_contactos(agenda):
    if agenda:
        print("\nLista de contactos:")
        for nombre,info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {info["telefono"]}")
            print(f"E-mail: {info["email"]}")
            print("-" * 20)
    else:
        print("La agenda aún está vacía")

def agenda_contactos():
    agenda = {}

    while True: # Se ejecuta siempre hasta que utilkicemos el break para salir del bucle
        mostrar_menu()
        opcion = input("Por favor elija una opción: ")

        if opcion == "1":
            agregar_contacto(agenda) 
        elif opcion == "2":
            eliminar_contacto(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            listar_contactos(agenda)
        elif opcion == "5":
            print("Saliendo de la agenda de contactos, ¡Hasta luego!")
            break
        else: 
            print("Por favor seleccione una opción válida (del 1 al 5)")


agenda_contactos()
