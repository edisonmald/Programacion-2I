import os

def crear_archivo_generico():
    with open("archivo_generico.txt", "w") as archivo:
        archivo.write("Archivo genérico creado.\n")
    print("Archivo 'archivo_generico.txt' creado.")

def crear_archivo_con_nombre():
    nombre = input("Ingresa el nombre del archivo (sin extensión): ") + ".txt"
    with open(nombre, "w") as archivo:
        archivo.write("Archivo creado con nombre personalizado.\n")
    print(f"Archivo '{nombre}' creado.")

def ingresar_informacion():
    nombre = input("Nombre del archivo al que deseas agregar información (con .txt): ")
    if os.path.exists(nombre):
        with open(nombre, "a") as archivo:
            texto = input("Escribe el texto a agregar: ")
            archivo.write(texto + "\n")
        print(f"Texto agregado a '{nombre}'.")
    else:
        print("El archivo no existe.")

def eliminar_archivo():
    archivos_txt = [f for f in os.listdir() if f.endswith(".txt")]
    if not archivos_txt:
        print("No hay archivos .txt para eliminar.")
        return
    print("Archivos disponibles para eliminar:")
    for i, archivo in enumerate(archivos_txt, start=1):
        print(f"{i}. {archivo}")
    opcion = int(input("Selecciona el número del archivo a eliminar: "))
    if 1 <= opcion <= len(archivos_txt):
        archivo_a_eliminar = archivos_txt[opcion - 1]
        os.remove(archivo_a_eliminar)
        print(f"Archivo '{archivo_a_eliminar}' eliminado.")
    else:
        print("Opción no válida.")

# Menú principal
def menu():
    opciones = {
        "1": crear_archivo_generico,
        "2": crear_archivo_con_nombre,
        "3": ingresar_informacion,
        "4": eliminar_archivo
    }

    for _ in range(10):  # Puedes cambiar 10 por el número de veces que quieras mostrar el menú
        print("\nMenú:")
        print("1. Crear archivo genérico")
        print("2. Crear archivo con nombre")
        print("3. Ingresar información a un archivo")
        print("4. Eliminar archivo")
        print("5. Salir")

        eleccion = input("Elige una opción: ")

        if eleccion == "5":
            print("Saliendo del programa.")
            break
        elif eleccion in opciones:
            opciones[eleccion]()
        else:
            print("Opción inválida.")

menu()
