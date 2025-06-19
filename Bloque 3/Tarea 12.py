# Agenda simple
agenda = {}
def agregar_contacto():
    nombre = input("Nombre del contacto: ")
    telefono = input("Teléfono: ")
    agenda[nombre] = telefono
    print(f"Contacto '{nombre}' agregado correctamente.")

def mostrar_contactos():
    if not agenda:
        print("La agenda está vacía.")
    else:
        print("Contactos en la agenda:")
        for nombre, telefono in agenda.items():
            print(f"- {nombre}: {telefono}")
        print()

def buscar_contacto():
    nombre = input("Nombre a buscar: ").strip()
    if nombre in agenda:
        print(f"{nombre}: {agenda[nombre]}")
    else:
        print(f"El contacto '{nombre}' no está en la agenda.")

def menu():
    opcion = ""
    while opcion != "4":
        print("Agenda de Contactos")
        print("1. Agregar contacto")
        print("2. Mostrar todos los contactos")
        print("3. Buscar contacto")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            mostrar_contactos()
        elif opcion == "3":
            buscar_contacto()
        elif opcion != "4":
            print("Opción no válida. Intenta de nuevo.\n")


menu()
