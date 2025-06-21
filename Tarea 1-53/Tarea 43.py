with open("mbox.txt", "r") as f:
    lineas = f.readlines()

num_lineas = len(lineas)
num_palabras = sum(len(linea.split()) for linea in lineas)
num_caracteres = sum(len(linea) for linea in lineas)

print("Líneas:", num_lineas)
print("Palabras:", num_palabras)
print("Caracteres:",num_caracteres)