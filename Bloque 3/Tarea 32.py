# Crea un archivo llamado 'texto.txt' con varias líneas antes de ejecutar este código.
with open("mbox.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())
