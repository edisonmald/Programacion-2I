# Leer el archivo archivo.txt
with open("archivo.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.strip())
