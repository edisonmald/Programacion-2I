from collections import Counter

# Leer archivo
with open("datos.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read().lower()

# Separar palabras
palabras = contenido.split()

# Contar palabras
conteo = Counter(palabras)

# Mostrar las 3 más comunes
print("Top 3 palabras más repetidas:")
for palabra, frecuencia in conteo.most_common(3):
    print(palabra, ":", frecuencia)
